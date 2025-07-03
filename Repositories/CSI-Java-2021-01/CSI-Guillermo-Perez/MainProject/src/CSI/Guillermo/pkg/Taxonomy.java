/**
 * 
 */
package csi.guillermo.pkg;

/**
 * @author guillermoperez
 *
 */
	public class Taxonomy {
		String domain;
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



		public String getClassis() {
			return classis;
		}



		public void setClassis(String classis) {
			this.classis = classis;
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



		public Taxonomy(String domain, String kingdom, String phylum, String classis, String order, String family,
				String genus, String species) {
			super();
			this.domain = domain;
			this.kingdom = kingdom;
			this.phylum = phylum;
			this.classis = classis;
			this.order = order;
			this.family = family;
			this.genus = genus;
			this.species = species;
		}
		public Taxonomy() {
			
		}


		String kingdom;
		String phylum;
		String classis;
		String order;
		String family;
		String genus;
		String species; 
		
		public String toString() {
			String s = String.format("""
					Domain: %s
					Kingdom: %s
					Phylum: %s
					Classis: %s
					Order: %s
					Family: %s
					Genus: %s
					Species: %s
					""", 
					domain,
					kingdom,
					phylum,
					classis,
					order,
					family,
					genus,
					species);
			return s;	
		}
		
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	}
	
