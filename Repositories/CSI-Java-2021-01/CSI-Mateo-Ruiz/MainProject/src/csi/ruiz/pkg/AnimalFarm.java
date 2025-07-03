package csi.ruiz.pkg;

public class AnimalFarm {
	static Animal[] animals;

	public static void main(String[] args) {
		animals    = new Animal[10];
		animals[0] = new Animal("Canary", 4, "Serinus canaria domestica", new Taxonomy("Eukaryote", "Animalia", "Aves","Passeriformes", "Fringillidae", "Carduelinae", "Serinus", "canaria"));
		animals[1] = new Animal("Cotorra", 5, "Amazona vittata", new Taxonomy("Eukaryote", "Animalia", "Chordata","Aves", "Psittaciformes", "Psittacidae", "Amazona", "Amazona vitata"));
		animals[2] = new Animal("Mountain Chicken", 6, "leptodactylus fallax", new Taxonomy("Eukaryote", "animalia","Chordata", "Amphibia", "anura", "leptodactylidae", "leptodactylus", "leptodactylus fallax"));
		animals[3] = new Animal("Platypus", 5, "Ornithorhynchus anatinus",new Taxonomy("Eukaryote", "animalia", "Chordata", "mammalia", "monotremata", "Ornithorhynchidae","Ornithorhynchus", "Ornithorhynchus anatius"));
		animals[4] = new Animal();
		animals[5] = new Animal("gnu", 7, "Connochaetes");
		animals[6] = new Animal("tapir", 11,"Tapiridae",new Taxonomy());
		//printAnimals();
		printEachAnimal();
		whileLoop();
		
	}
	//Hacen lo mismo
	public static void printAnimals() {
		for (int i = 0; i < animals.length; i++) {
			System.out.println("Animal: "+i);
		System.out.println(animals[i]);	
		}
	}
	public static void printEachAnimal() {
		for (Animal a : animals){
		    System.out.println(a);
		}
	}
	//While loop no hace lo mismo tienes que poner el break o es infinito.
	public static void whileLoop() {
		int x = 0;
		while(x<100) {
		  x++;
		if(x==10)
			break;
		System.out.println(x);
		}	
	}
}

