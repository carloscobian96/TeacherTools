package csi.quiros.pkg;

public class AnimalFarm {
	static Animal[] animals;

	public static void main(String[] args) {
		animals = new Animal[10];
		animals[0] = new Animal("Horse", 30, "Equus caballus", new Taxonomy("Eukaryote", "Animalia", "Chordate",
				"Mammalia", "Perissodactyla", "Equidae", "Equus Linnaeus", "Equus caballus"));
		animals[1] = new Animal("Goldfish", 3, "Carassius auratus", new Taxonomy("Eukaryote", "Animalia", "Chordate",
				"Actinopterygii", "Cypriniformes", "Cyprinidae", "Carassius", "Carassius auratus"));
		animals[2] = new Animal("Aye-aye", 22, "Daubentonia madagascariensis", new Taxonomy("Eukaryote", "Animalia",
				"Chordata", "Mammalia", "Primates", "Strepsirrhini", "Daubentonia", "D.madagascariensis"));
		animals[3] = new Animal("Capybara", 9, "Hydrochoerus hydrochaeris", new Taxonomy("Eukaryote", "Animalia",
				"Chordate", "Mammalia", "Rodentia", "Caviidae", "	Hydrochoerus", "Hydrochoerus hydrochaeris"));
		animals[4] = new Animal();
		animals[5] = new Animal("Dwarf Lemur", 19, "Cheirogaleus");
		animals[6] = new Animal("Japanese white crucian carp", 3, "Carassius cuvieri", new Taxonomy());
		//printAnimals();
		//printEachAnimal();
		additionSubtraction();
	}

	public static void printAnimals() {
		for (int i = 0; i < animals.length; i++) {
			System.out.println("Animal: "+i);
			System.out.println(animals[i]);
			
		}
		
	}
	public static void printEachAnimal() {
		for(Animal a : animals){
			  System.out.println(a);
			}
		
		
		
	}
	public static void additionSubtraction() {
		int x = 100;
		while(x>0) {
			System.out.print(x);
			if(x==50) {
			
				break;
				
			}
			x--;
		}
				
		
		
	}
		
}
		


