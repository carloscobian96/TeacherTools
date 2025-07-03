package csi.ochoa.pkg;

public class Taxonomy {

	String domain;
    String species;
    String genus;
    String kingdom;
    String phylum;
    String classis;
    String order;
    String family;

    
    
    //  Getters and Setters  
    public String getDomain(){
        return domain;
    }
    public void setDomain(String domain){
        this.domain = domain;
    }
    
    public String getSpecies(){
        return species;
    }
    public void setSpecies(String species){
        this.species = species;
    }
    
    public String getGenus(){
        return genus;
    }
    public void setGenus(String genus){
        this.genus = genus;
    }
    public String getKingdom(){
        return kingdom;
    }
    public void setKingdom(String kingdom){
        this.kingdom = kingdom;
    }
    public String getClassis(){
        return classis;
    }
    public void setClassis(String classis){
        this.classis = classis;
    }
    public String getPhylum(){
        return phylum;
    }
    public void setPhylum(String phylum){
        this.phylum = phylum;
    }
    public String getOrder(){
        return order;
    }
    public void setOrder(String order){
        this.order = order;
    }
    public String getFamily(){
        return family;
    }
    public void setFamily(String family){
        this.family = family;
    }
    
   
    
    
    //Constructors
    
    public Taxonomy(String domain,String kingdom, String phylum, String classis, String order, String family, String genus, String species) {
		this.genus = genus;
		this.kingdom = kingdom;
		this.classis = classis;
		this.species = species;
		this.phylum = phylum;
		this.order = order;
		this.family = family;
		this.domain = domain;
	}
    public Taxonomy() {

	}
   
    
	
public String toString() {
		
		String s = String.format(""" 
				Genus: %s
				Species: %s
				Classis: %s
				Domain: %s
				Kingdom: %s
				Phylum: %s
				Order: %s
				Family: %s
				""",
				genus,
				species,
				classis,
				domain,
				kingdom,
				phylum,
				order,
				family);
				
				return s;
				
	}
	
	
	
	
	
	
	
}
















