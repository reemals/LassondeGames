class Item {
	constructor(id, x, y, type) {
		this.id = id;
		this.x = x;
		this.y = y;
		this.type = type;
	}
}

exports.itemsCount = function(items, type) {
	return 10;
}

exports.asteroidItems = [
	new Item(0, 2, 19, 0),
	new Item(1, 1, 2, 0),
	new Item(2, 2, 13, 2),
	new Item(3, 5, 18, 4),
	new Item(4, 4, 9, 3),
	new Item(5, 20, 10, 3),
	new Item(6, 7, 7, 0),
	new Item(7, 19, 15, 1),
	new Item(8, 11, 9, 1),
	new Item(9, 13, 15, 0),
	new Item(10, 8, 3, 2),
	new Item(11, 20, 2, 3),
	new Item(12, 13, 20, 4),
	new Item(12, 14, 8, 4)
]
