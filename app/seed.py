from app.database import SessionLocal, engine, Base
from app.models import Cliente, Pedido

Base.metadata.create_all(bind=engine)
db = SessionLocal()

if db.query(Cliente).count() == 0:
    N = 5000
    clientes = [Cliente(nome=f"Cliente {i}", email=f"c{i}@example.com") for i in range(N)]
    db.add_all(clientes)
    db.commit()

    pedidos = [Pedido(valor=100 + i, cliente_id=clientes[i].id) for i in range(N)]
    db.add_all(pedidos)
    db.commit()
    print(f"Populado: {db.query(Cliente).count()} clientes, {db.query(Pedido).count()} pedidos")
else:
    print("Banco já populado")
db.close()