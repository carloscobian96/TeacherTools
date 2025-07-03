package csi.ochoa.pkg;

public class AnimalFarm {

	static Animal[] animals;

	public static void main(String[] args) {

		animals = new Animal[10];

		animals[0] = new Animal("Shark", 6, "Selachimorpha", new Taxonomy("Eukaryote", "Animalia", "Chordata",
				"	Chondrichthyes", "Lamniformes ", "Lamnidae", "Carcharodon", "Carcharodon carcharias"));
		animals[1] = new Animal("Tiger", 7, "Panthera tigris", new Taxonomy("Eukaryote", "Animalia", "Chordate",
				"Mammal", "Carnivora", "	Felidae", "	Panthera", "Panthera tigris"));
		animals[2] = new Animal("Lion", 4, "Panthera leo", new Taxonomy("Eukaryote", "Animalia", "Chordate", "Mammal",
				"Carnivora", "Felidae", "Panthera", "Panthera leo"));
		animals[3] = new Animal("Panther", 5, "Panthera pardus", new Taxonomy("Eukaryote", "Animalia", "Chordate",
				"Mammal", "Carnivora", "Felidae", "Panthera", "Panthera pardus"));
		animals[4] = new Animal();
		animals[5] = new Animal("Dog", 2, "Canis lupus familiaris");
		animals[6] = new Animal("Horse", 8, "Equus caballus", new Taxonomy());

		
		
//		animals[4] = new Animal("Wolf", 3, "Canis Lupus", new Taxonomy("Eukaryote", "Animalia", "Chordate", "Mammal",
//				"Carnivora", "Canidae", "Canis", "Canis Lupus"));
//		animals[5] = new Animal("Leopard", 7, "Panthera pardus", new Taxonomy("Eukaryote", "Animalia", "Chordate",
//				"Mammal", "Carnivora", "Felidae", "Panthera", "Panthera pardus"));

		printAnimals();

	}

	public static void printAnimals() {

		for (int i = 0; i < animals.length; i++) {

			System.out.println("Animal: " + i);
			
			System.out.println(animals[i]);

				
			for(Animal a : animals){
				  System.out.println(a);
				}
			
		}

	}

// domain,kingdom,phylum,class,order,family,genus,species

}
