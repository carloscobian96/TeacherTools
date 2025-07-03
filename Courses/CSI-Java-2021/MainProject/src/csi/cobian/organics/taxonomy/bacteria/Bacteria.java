/**
 * 
 */
package csi.cobian.organics.taxonomy.bacteria;

import csi.cobian.organics.Organism;
import csi.cobian.organics.taxonomy.Domain;

/**
 * @author carlos.cobian
 *
 */
public class Bacteria extends Organism implements Domain {

	public Bacteria() {
		this.name = "Some Bacteria";
		this.taxonomy.domain = this.getClass().getSimpleName();

		this.multicellular = false;
		this.reproduction = new String[] { "binary fission" };
		this.nutrition = new String[] { "photosynthesis", "decomposition" };
		this.locomotion = new String[] { "flagellar" };
	}

	@Override
	public void reproduce() {
		super.reproduce();
	}
}
