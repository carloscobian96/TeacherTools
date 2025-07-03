package csi.cobian.src;

public class Animal {
    //	Fields
    String name;
    int age;
    String scientificName;
    Taxonomy taxonomy;
	
    //  Constructors
	public Animal(String name, int age, String scientificName) {
		this.name = name;
		this.age = age;
		this.scientificName = scientificName;
	}

	public Animal() {
	}

	public Animal(String name, int age, String scientificName, Taxonomy taxonomy) {
		this.name = name;
		this.age = age;
		this.scientificName = scientificName;
		this.taxonomy = taxonomy;
	}
	
    //  Getters and Setters  
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    
    public int getAge(){
        return age;
    }
    public void setAge(int age){
        this.age = age;
    }
    
    public String getScientificName(){
        return scientificName;
    }
    public void setScientificName(String scientificName){
        this.scientificName = scientificName;
    }

    public Taxonomy getTaxonomy(){
        return taxonomy;
    }
    public void setTaxonomy(Taxonomy taxonomy){
        this.taxonomy = taxonomy;
    }
    
    public String toString() {
    	String s = String.format("""
    			Common Name: %s
    			Age: %d
    			Scientific name: %s
    			Taxonomy: %s
    			""", 
    			name,
    			age,
    			scientificName,
    			taxonomy);
    	return s;	
    }
}


