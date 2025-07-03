package csi.quiros.pkg;

public class Taxonomy {
	String domain;
	String kingdom;
	String phylum;
	String classius;
	String order;
	String family;
	String genus;
	String species;

	public Taxonomy(String domain, String kingdom, String phylum, String classius, String order, String family,
			String genus, String species) {
		this.domain = domain;
		this.kingdom = kingdom;
		this.phylum = phylum;
		this.classius = classius;
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

	public String getClassius() {
		return classius;
	}

	public void setClassius(String classius) {
		this.classius = classius;
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

	public String toString() {
		String t = String.format(
				"Domain: %s \n Kingdom: %s \n Phylum: %s \n Class: %s \n Order: %s \n Family: %s \n Genus: %s \n Species: %s \n",
				domain, kingdom, phylum, classius, order, family, genus, species);
		return t;
	}
}
