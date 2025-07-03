package csi.lopez.pkg;

public class AnimalFarm {
	static Animal[] animals;
    
	public static void main(String[] args) {
		
		animals = new Animal[10];
		
		animals[0] = new Animal(new Taxonomy("Eukaryote", "Animalia", "Chordata", "Mammalia", "Carnivora", "Felidae", "Felis","Felis Catus"),"Cat", 3, "Felis catus");	;
		animals[1] = new Animal(new Taxonomy("Eukaryote", "Animalia", "Chordata", "Chondrichthyes", "Carcharhiniformes", "Carcharhinidae", "Galeocerdo", "G. cuvier"),"Tiger Shark", 4, "Galeocerdo cuvier");;
		animals[2] = new Animal(new Taxonomy("Eukaryote", "Animalia", "Chordata", "Aves", "Psittaciformes", "Psittacidae", "Amazona", "A. vittata"),"Cotorra Puertoriqueña", 2, "Amazona vittata");
		animals[3] = new Animal(new Taxonomy("Eukaryote", "Animalia", "Chordata", "Actinopteygii", "Scorpaeniformes", "Scorpaenidae", "Pterois", "Pterois volitans"), "Lion Fish", 1, "Pterois");
		animals[4] = new Animal();
		animals[5] = new Animal("Lion", 4, "Panthera leo");
		animals[6] = new Animal(new Taxonomy(), "Wolf", 10, "Canis Lupus");
		
		
//		System.out.println(animals[0]);
//		System.out.println(animals[1]);
//		System.out.println(animals[2]);
//		System.out.println(animals[3]);
//		System.out.println(animals[4]);
		
//		printAnimals();
		printEachAnimal();
		
	}
	
	
	public static void printAnimals() {

		for(int i = 0; i < animals.length; i++) {
			
			System.out.println("Animal: " + i);
			System.out.println(animals[i]);
		}	
	}
	
	public static void printEachAnimal() {
		
		for(Animal a : animals){
			System.out.println(a);
		}
	}
	
	
	
}
