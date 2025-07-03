package csi.cobian.organics.taxonomy;

public class Taxonomy {
	// Fields
	public String domain;
	public String kingdom;
	public String phylum;
	public String classs;
	public String order;
	public String family;
	public String genus;
	public String species;

	public Taxonomy(String domain, String kingdom, String phylum, String classs, String order, String family,
			String genus, String species) {
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

	@Override
	public String toString() {
		String tomas = String.format("""

				\t Domain: %s
				\t Kingdom: %s
				\t Phylum: %s
				\t Classis: %s
				\t Order: %s
				\t Family: %s
				\t Genus: %s
				\t Species: %s """, domain, kingdom, phylum, classs, order, family, genus, species);
		return tomas;
	}

}
