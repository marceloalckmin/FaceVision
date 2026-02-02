import os
import pickle
import cv2
import numpy as np
from insightface.app import FaceAnalysis

app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(320, 320))

BASE_FOTOS = "fotos"
SAIDA = "data/embeddings.pkl"

base = []

for pessoa in os.listdir(BASE_FOTOS):
    pasta = os.path.join(BASE_FOTOS, pessoa)
    if not os.path.isdir(pasta):
        continue

    nome, matricula = pessoa.split("_") if "_" in pessoa else (pessoa, None)

    embeddings = []

    for img_name in os.listdir(pasta):
        img = cv2.imread(os.path.join(pasta, img_name))
        faces = app.get(img)
        if len(faces) == 0:
            continue
        emb = faces[0].embedding
        emb = emb / np.linalg.norm(emb)
        embeddings.append(emb)

    if embeddings:
        emb_medio = np.mean(embeddings, axis=0)
        emb_medio /= np.linalg.norm(emb_medio)

        base.append({
            "nome": nome,
            "matricula": matricula,
            "embedding": emb_medio
        })

with open(SAIDA, "wb") as f:
    pickle.dump(base, f)

print(f"Base criada com {len(base)} identidades")
