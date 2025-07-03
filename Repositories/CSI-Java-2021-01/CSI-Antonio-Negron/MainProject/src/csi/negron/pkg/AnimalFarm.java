package csi.negron.pkg;

public class AnimalFarm {

	// Field
	static Animal[] animals;
	
	

	// Main Method
	public static void main(String[] args) {
	
		animals = new Animal[10];

		animals[0]=new Animal("Coqui",3,"Eleutherodactylus coqui",new Taxonomy("Animal","Chordate","Anura"," Eleutherodactylidae","Common Coqui","Eleuths","Puerto Rican Coqui","Eukaryote"));
		animals[1]=new Animal("Canadian Goose",13,"Branta Canadensis",new Taxonomy("Animal","Chordate","Anseriformes","Anatidae","Giant","Brent Geese","Giant Canada Goose","Eukaryote"));
		animals[2]=new Animal("Domestic Pig",16,"Sus Scrofa Domesticus",new Taxonomy("Animal","Chordate","Artiodactyla","Suidae","S.domesticus","Sus","Eukaryote","Sus scrofa domesticus"));
		animals[3]=new Animal("Sheep",7,"Ovis",new Taxonomy("Animal","Chordate","Ovis","Bovidae","Dorper","Ovis","Stone Sheep","Eukaryote"));
        animals[4]=new Animal();
        animals[5]=new Animal("Bornean Bearded Pig",5,"Sus Barbatus");
        animals[6]=new Animal("Bighorn Sheep",9,"Ovis Canadensis", new Taxonomy());
		
		//printAnimals();
		PrintEachAnimal();
	} 
	
	public static void printAnimals() {
		
		for(int i = 0;i<animals.length;i++) {
			
			System.out.println("Animal: " + i);
			
			System.out.println(animals[i]);
			
			
				
			}
			
			}

		
	
	public static void PrintEachAnimal() {
		
		for(Animal a: animals) {
	
			System.out.println(a);	
			
		}
	}
	}

