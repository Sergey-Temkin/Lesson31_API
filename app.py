from flask import Flask, request , jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Pet list
pet1 = {"id":1, "name":"Dixie", "age":1,"image":"https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg"}
pet2 = {"id":2, "name":"Charlie","age":2,"image":"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"}
#      {"id":3, "name":"Rexie","age":3,"image":"https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"}
pets = [pet1, pet2]

# Add pet
@app.route("/pets", methods=["POST"])
def add_pet():
    new_pet = request.get_json()
    pets.append(new_pet)
    return jsonify({"Result": "Pet added successfully"}), 200

# Display pet list
@app.route("/pets")
def pets_list():
    return pets ,200


# Display single pet    
@app.route("/pets/<id>/")
def single_pet(id):
    try:
        for pet in pets:
            if pet["id"] == int(id):
                return pet
    except:
        print("Error in id")
    return jsonify({"Result":"Pet not found"}), 400

# Update pet by ID
@app.route('/pets/<int:id>', methods=['PUT'])
def update_pet(id):
    for pet in pets:
        if pet['id'] == int(id):
            updated_pet = request.get_json()
            pets.remove(pet)
            pets.append(updated_pet)
            return jsonify({"Result": "Pet updated successfully"}), 200
    return jsonify({"Result":"Pet not found"}), 400

# Delete a pet by ID
@app.route('/pets/<int:id>', methods=['DELETE'])
def delete_pet(id):
    global pets
    pets = [pet for pet in pets if pet['id'] != id]
    return jsonify({'result': 'Pet deleted successfully'}), 200


# Run the app only if this script is executed(Not imported)
if __name__ == "__main__":
    app.run(debug=True)