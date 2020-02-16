class Person {
	constructor(name, age) {
		this.name = name;
		this.age = age;
	}

	get details() {
		return `Person's name is ${this.name} and age is ${this.age}`
	}

	set details(name, age) {
		this._name = name;
		this._age = age;
	}
}

const person1 = new Person("Nitin", 30);

console.log(person1.details());
