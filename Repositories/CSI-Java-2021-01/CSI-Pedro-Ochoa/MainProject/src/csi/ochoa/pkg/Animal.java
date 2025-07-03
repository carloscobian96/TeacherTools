package csi.ochoa.pkg;

public class Animal {

//	Fields
	String name;
	int age;
	String scientificName;
	Taxonomy taxonomy;
	

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
		return scientificName;
	}

	public void setScientificName(String scientificName) {
		this.scientificName = scientificName;
	}

	public Animal(String name, int age, String scientificName) {
		this.name = name;
		this.age = age;
		this.scientificName = scientificName;
	}

	public Animal(String name, int age, String scientificName, Taxonomy taxonomy) {
		this.name = name;
		this.age = age;
		this.scientificName = scientificName;
		this.taxonomy=taxonomy;
	}

	public Animal() {

	}

	public Taxonomy getTaxonomy() {
		return taxonomy;
	}

	public void setTaxonomy(Taxonomy taxonomy) {
		this.taxonomy = taxonomy;
	}

	public String toString() {

		String s = String.format("""
				Name: %s
				Age: %d
				Scientific Name: %s
				Taxonomy: %s
				""", name, age, scientificName, taxonomy);

		return s;

	}

//  Main Method
	public static void main(String[] args) {

		Animal a = new Animal();
		a.setName("marmoset");
		a.setAge(6);
		a.setScientificName("Callithrix jacchus");

		System.out.println("Name: " + a.getName());
		System.out.println("Age: " + a.getAge());
		System.out.println("Scientific Name: " + a.getScientificName());

		Animal a2 = new Animal("Monkey", 5, "Cercopithecidae");

		System.out.println("Name: " + a2.getName());
		System.out.println("Age: " + a2.getAge());
		System.out.println("Scientific Name: " + a2.getScientificName());
		System.out.println();

		Taxonomy t = new Taxonomy("Eukaryote", "Gorilla", "mammal", "Eastern", "Chordate", "Primate", "Great Apes", "Jungle");

		Animal a3 = new Animal("Gorilla", 7, "Gorilla", t);
		System.out.println(a3);
        System.out.println("Name: " + a3.getName());
        System.out.println("Age: " + a3.getAge());
        System.out.println("Scientific Name: " + a3.getScientificName());
      
       
       System.out.println("Genus: " + a3.getTaxonomy().getGenus());
       System.out.println("Domain: " + a3.getTaxonomy().getDomain());
       System.out.println("Species: " + a3.getTaxonomy().getSpecies());
       System.out.println("Classis: " + a3.getTaxonomy().getClass());

		a3.getTaxonomy().getOrder();

	}

}