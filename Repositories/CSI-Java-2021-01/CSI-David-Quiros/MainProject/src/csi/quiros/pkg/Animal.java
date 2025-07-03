package csi.quiros.pkg;

public class Animal {

	//	Fields
	    String name;
	    int age;
	    String scientificName;
	    Taxonomy taxonomy;
		
	//  Constructors
		public Animal(String name,int age,String scientificName) {
			this.name = name;
			this.age = age;
			this.scientificName = scientificName;}

		
		public Animal(String name,int age,String scientificName,Taxonomy taxonomy) {
			this.name = name;
			this.age = age;
			this.scientificName = scientificName;
			this.taxonomy = taxonomy;

		}
		public Animal() {
			
		}
		
	    //  Getters and Setters  
	    public String getName(){
	        return name;
	    }
	    public Taxonomy getTaxonomy(){
	        return taxonomy;
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
	        
	        
	    public String toString() {
	    		String tomas = String.format("Name: %s \n age: %s \n scientificName: %s \n Taxonomy: %s \n ",name,age,scientificName,taxonomy);
	    				
	    									
	    			return tomas;
	    }		
	        
	        
	    //  Main Method
	    public static void main(String[] args){
	        Animal a = new Animal(); 
	        a.setName("Aye-aye");
	        a.setAge(22);  
	        a.setScientificName("Daubentonia madagascariensis");
	        
	        System.out.println("Name: " + a.getName());
	        System.out.println("Age: " + a.getAge());
	        System.out.println("Scientific Name: " + a.getScientificName());
	        
	        Animal a2 = new Animal("Goldfish",3,"Carassius auratus");
	        
	        System.out.println("           ");
	        System.out.println("Name: " + a2.getName());
	        System.out.println("Age: " + a2.getAge());
	        System.out.println("Scientific Name: " + a2.getScientificName());
	        System.out.println("           ");
	        
	        
	        Taxonomy t = new Taxonomy("Eukaryote","Animalia","Chordate","Mammalia","Perissodactyla","Equidae","Equus Linnaeus","Equus caballus Linnaeus");
    		
	        Animal a3 = new Animal ("Horse",30,"Equus caballus",t);
	        
	        System.out.println("Name: " + a3.getName());
	        System.out.println("Age: " + a3.getAge());
	        System.out.println("Scientific Name: " + a3.getScientificName());
	        System.out.println("           ");
	    	System.out.println("Horse Taxonomy");
	    	System.out.println("           ");
	    	System.out.println("Domain:" + a3.getTaxonomy().getDomain());
	    	System.out.println("Kingdom:" + a3.getTaxonomy().getKingdom());
	    	System.out.println("Phylum:" + a3.getTaxonomy().getPhylum());
	    	System.out.println("Class:" + a3.getTaxonomy().getClassius());
	    	System.out.println("Order:" + a3.getTaxonomy().getOrder());
	    	System.out.println("Family:" + a3.getTaxonomy().getFamily());
	    	System.out.println("Genus:" + a3.getTaxonomy().getGenus());
	    	System.out.println("Species:" + a3.getTaxonomy().getSpecies());
	    	
	    	System.out.println();
	    	System.out.println(a3);
	    }
	 
	    

    }
    

	


