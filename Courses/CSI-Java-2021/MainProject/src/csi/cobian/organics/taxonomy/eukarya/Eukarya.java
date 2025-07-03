/**
 * 
 */
package csi.cobian.organics.taxonomy.eukarya;

import csi.cobian.organics.Organism;
import csi.cobian.organics.taxonomy.Domain;

/**
 * @author carlos.cobian
 *
 */
public class Eukarya extends Organism implements Domain {

	public Eukarya() {
		this.name = "Some Eukaryotic Organism";
		this.taxonomy.domain = this.getClass().getSimpleName();

		multicellular = true;
		reproduction = new String[] { "mitosis", "meiosis" };
		nutrition = new String[] { "photosynthesis", "glycolysis" };
		locomotion = new String[] { "flagella", "ciliary", "amoeboid", "citric acid cycle",
				"oxidative phosphorylation" };
	}

	@Override
	public void reproduce() {
		super.reproduce();

	}
}
