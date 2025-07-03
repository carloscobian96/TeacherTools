package csi.cobian.src;

public class Taxonomy {
    //	Fields
    String domain;
    String kingdom;
    String phylum;
    String classs;
    String order;
    String family;
    String genus;
    String species;
    
    
	public Taxonomy(String domain, String kingdom, String phylum, String classs, String order, String family,
			String genus, String species) {
		super();
		this.domain = domain;
		this.kingdom = kingdom;
		this.phylum = phylum;
		this.classs = classs;
		this.order = order;
		this.family = family;
		this.genus = genus;
		this.species = species;
	}
	public Taxonomy() {
	}
	public String getDomain() {
		return domain;
	}
	public void setDomain(String domain) {
		this.domain = domain;
	}
	public String getKingdom() {
		return kingdom;
	}
	public void setKingdom(String kingdom) {
		this.kingdom = kingdom;
	}
	public String getPhylum() {
		return phylum;
	}
	public void setPhylum(String phylum) {
		this.phylum = phylum;
	}
	public String getClasss() {
		return classs;
	}
	public void setClasss(String classs) {
		this.classs = classs;
	}
	public String getOrder() {
		return order;
	}
	public void setOrder(String order) {
		this.order = order;
	}
	public String getFamily() {
		return family;
	}
	public void setFamily(String family) {
		this.family = family;
	}
	public String getGenus() {
		return genus;
	}
	public void setGenus(String genus) {
		this.genus = genus;
	}
	public String getSpecies() {
		return species;
	}
	public void setSpecies(String species) {
		this.species = species;
	}
	@Override
	public String toString(){
		String tomas = String.format("""
				
			\t Domain: %s
			\t Kingdom: %s
			\t Phylum: %s
			\t Classis: %s
			\t Order: %s
			\t Family: %s
			\t Genus: %s 
			\t Species: %s """,domain,kingdom,phylum,classs,order,family,genus,species);
		return tomas;
	}

    
}


