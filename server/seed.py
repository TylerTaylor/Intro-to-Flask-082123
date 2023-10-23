from app import app
from models import db, Shoe, Tree

with app.app_context():

    print("Deleting existing objects...")
    
    Shoe.query.delete()
    Tree.query.delete()

    shoe1 = Shoe(brand="Nike", size="13", color="Black", name="Air Force", type="casual")
    shoe2 = Shoe(brand="Adidas", size="10", color="White", name="stan smith", type="casual")

    tree1 = Tree(leaves=312, evergreen=True, fruit=False, type="pine")
    
    shoes = [shoe1, shoe2]

    db.session.add_all(shoes)

    db.session.add(tree1)

    db.session.commit()

    print("Everything added!")