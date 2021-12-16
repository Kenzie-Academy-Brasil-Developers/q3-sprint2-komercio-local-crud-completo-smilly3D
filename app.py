from flask import Flask, request, jsonify
from produtos import produtos

app= Flask(__name__)



@app.get("/products")
def list_products():
    return jsonify(produtos),200

@app.get("/products/<product_id>")
def get(product_id: int):
    # id_filter = [item for item in produtos if item["id"] == int(product_id)]
    id_filter = produtos[int(product_id)-1]
    return jsonify(id_filter),200 

@app.post('/products')
def registrar_nome():
    data = request.get_json()
    data["id"] = (len(produtos) + 1)
    novo_nome = data.get('name')
    produtos.append(data)

    return {'msg': f'Usuário {novo_nome} cadastrado!'}, 201

@app.patch("/products/<product_id>")
def update(product_id: int):
    data = request.get_json()
    produtos[int(product_id)-1] = { **produtos[int(product_id)-1], **data}
    return "",204

@app.delete("/products/<product_id>")
def delete(product_id: int):
    del produtos[int(product_id)-1]
    return "",204
