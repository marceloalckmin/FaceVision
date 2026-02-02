import pickle
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from mqtt.pub_presenca import pub_presenca

CONFIDENCE_THRESHOLD = 0.6

def cosine(a, b):
    return np.dot(a, b)

with open("data/embeddings.pkl", "rb") as f:
    base = pickle.load(f)

app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(320, 320))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = app.get(frame)

    for face in faces:
        emb = face.embedding
        emb = emb / np.linalg.norm(emb)

        best = None
        best_sim = -1

        for p in base:
            sim = cosine(emb, p["embedding"])
            if sim > best_sim:
                best_sim = sim
                best = p

        x1, y1, x2, y2 = face.bbox.astype(int)

        if best_sim >= CONFIDENCE_THRESHOLD:
            label = f"{best['nome']} ({best_sim:.2f})"
            if best["matricula"]:
                pub_presenca({
                    "nome": best["nome"],
                    "matricula": best["matricula"],
                    "sala": "LAB-101",
                    "materia": "Visao Computacional"
                })
        else:
            label = "Desconhecido"

        cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame, label, (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.imshow("Reconhecimento", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
