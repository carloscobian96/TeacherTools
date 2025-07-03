package csi.negron.pkg;

public class Taxonomy {
	String phylum;
	String order;
	String family;
	String species;
	String genus;
	String subspecies;
	String domain;
	String kingdom;

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

	public String getSpecies() {
		return species;
	}

	public void setSpecies(String species) {
		this.species = species;
	}

	public String getGenus() {
		return genus;
	}

	public void setGenus(String genus) {
		this.genus = genus;
	}

	public String getSubspecies() {
		return subspecies;
	}

	public void setSubspecies(String subspecies) {
		this.subspecies = subspecies;
	}

	public Taxonomy(String kingdom, String phylum, String order, String family, String species, String genus,
			String subspecies, String domain) {
		super();
		this.kingdom = kingdom;
		this.phylum = phylum;
		this.order = order;
		this.family = family;
		this.species = species;
		this.genus = genus;
		this.subspecies = subspecies;
		this.domain = domain;

	}
	public Taxonomy() {
		super();
	}

	public String toString() {
		String s = String.format("""
				
				Kingdom: %s
				Phylum: %s
				Order: %s
				Family: %s
				Species: %s
				Genus: %s
				Subspecies: %s
				Domain: %s
				""", this.kingdom, this.phylum, this.order, this.family, this.species, this.genus,this.subspecies, this.domain );
		return s;
	}
}
