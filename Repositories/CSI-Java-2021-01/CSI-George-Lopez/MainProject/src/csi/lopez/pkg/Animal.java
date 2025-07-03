package csi.lopez.pkg;


public class Animal {
	//	Fields
    String name;
    int age;
    String scientificName;
    Taxonomy taxonomy;
    
    
    public Animal(String name,int age, String scientificName) {
		this.name = name;
		this.age = age;
		this.scientificName = scientificName;
	}
	public Animal() {}
	
	public Animal(Taxonomy taxonomy, String name, int age, String scientificName) {
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
    
    public Taxonomy getTaxonomy() {
    	return taxonomy;
    }
    
    public String toString() {
   	    String s = String.format("name:  %s \n Age: %d \n ScientificName: %s \n Taxomony: %s \n",name, age, scientificName, taxonomy);
    	return s;
   }
   
    
    
    public static void main(String[] args) {
    	Animal a = new Animal();
    	a.setName("Tigre");
    	a.setAge(9);
    	a.setScientificName("Panthera Tigris");
    	
    	
    	System.out.println("Name: " + a.getName());
        System.out.println("Age: " + a.getAge());
        System.out.println("Scientific Name: " + a.getScientificName());
        
        
        Animal a2 = new Animal("Cat", 3, "Felis catus");
        
        System.out.println("Name:" + a2.name);
        System.out.println("Age:" + a2.age);
        System.out.println("Scientific Name:" + a2.scientificName);
        
        
        
                
        Taxonomy taxomony  = new Taxonomy("Eukaryote", "Animalia", "Chordata", "Mammalia", "Carnivora", "Felidae", "Genus","Felis Catus");
        
        Animal a3 = new Animal(taxomony, "Cat", 4, "Felis Catus");
   
        a3.getTaxonomy().getDomain();
        a3.getTaxonomy().getKingdom();        
        a3.getTaxonomy().getPhylum();

        
        System.out.println("Domain: " + a3.getTaxonomy().getDomain());
        System.out.println("Kingdom: " + a3.getTaxonomy().getKingdom());
        System.out.println("Phylum: " + a3.getTaxonomy().getPhylum());
        System.out.println();
        System.out.println(a3);
        


        

    }  
    
    
}
