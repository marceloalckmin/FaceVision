import pickle
import numpy as np
import cv2
from insightface.app import FaceAnalysis

BASE = "data/embeddings.pkl"
FOTO = "nova_foto.jpg"

app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(320, 320))

with open(BASE, "rb") as f:
    base = pickle.load(f)

img = cv2.imread(FOTO)
faces = app.get(img)
emb = faces[0].embedding
emb = emb / np.linalg.norm(emb)

base.append({
    "nome": "NovoAluno",
    "matricula": "202099999",
    "embedding": emb
})

with open(BASE, "wb") as f:
    pickle.dump(base, f)

print("Aluno adicionado!")
