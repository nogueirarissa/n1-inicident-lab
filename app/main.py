from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Pedido

app = FastAPI(title="Pedidos API — Lab de Incidente")

@app.on_event("startup")
def criar_tabelas():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/pedidos")
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = db.query(Pedido).limit(5000).all()  # 1 query
    resultado = []
    for p in pedidos:
        resultado.append({
            "pedido_id": p.id,
            "valor": p.valor,
            "cliente": p.cliente.nome,  # ⚠️ N queries aqui (N+1)
        })
    return resultado

@app.get("/health")
def health():
    return {"status": "ok"}