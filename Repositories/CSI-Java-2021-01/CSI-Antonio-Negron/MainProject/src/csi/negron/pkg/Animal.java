package csi.negron.pkg;

public class Animal {
	// Fields
	String name;
	int age;
	String scientificname;
	Taxonomy taxonomy;
	
    //  Constructors
	public Animal(String name,int age, String scientificname) {
		this.name = name;
		this.age = age;
		this.scientificname = scientificname;
	}
	public Animal (String name,int age, String scientificname, Taxonomy taxonomy) {
		this.name = name;
		this.age = age;
		this.scientificname = scientificname;
		this.taxonomy = taxonomy;
	}
	public Animal () {
		
	}

	// Getters and Setters
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getScientificName() {
		return scientificname;
	}

	public Taxonomy getTaxonomy() {
		return taxonomy;
	}

	public void setScientificName(String scientificName) {
		this.scientificname = scientificName;
	}
	
	public String toString() {
    	String s = String.format("""
    			Name: %s
    			Age: %d
    			ScientificName: %s
    			Taxonomy: %s
    			
    			""", 
    			this.name,
    			this.age,
    			this.scientificname,
    			this.taxonomy);
    	return s;	
    }

//  Main Method
	public static void main(String[] args) {
		Animal a = new Animal();
		a.setName("Coqui");
		a.setAge(3);
		a.setScientificName("Eleutherodactylus coqui");

		System.out.println("Name: " + a.getName());
		System.out.println("Age: " + a.getAge());
		System.out.println("Scientific Name: " + a.getScientificName());
		
		
		Animal a2 = new Animal("Canadian Goose",13, "Branta Canadensis");


		System.out.println("Name: " + a2.getName());
		System.out.println("Age: " + a2.getAge());
		System.out.println("Scientific Name: " + a2.getScientificName());
		
		Taxonomy t3 = new Taxonomy("Animal","Chordate","Artiodactyla","Suidae","S.domesticus","Sus","Eukaryote","Sus scrofa domesticus");
		
		Animal a3 = new Animal("Domestic Pig",16,"Sus scrofa domesticus",t3);
		System.out.println(a3);
//		System.out.println("Name: " + a3.getName());
//		System.out.println("Age: " + a3.getAge());
//		System.out.println("Scientific Name: " + a3.getScientificName());
//		
//		
//		System.out.println("Family: " + a3.getTaxonomy().getFamily());
//		System.out.println("Order: " + a3.getTaxonomy().getOrder());
//		System.out.println("Genus: " + a3.getTaxonomy().getGenus());
//		
		

	}

}
