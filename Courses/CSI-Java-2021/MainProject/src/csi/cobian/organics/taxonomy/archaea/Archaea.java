/**
 * 
 */
package csi.cobian.organics.taxonomy.archaea;

import csi.cobian.organics.Organism;
import csi.cobian.organics.taxonomy.Domain;

/**
 * @author carlos.cobian
 *
 */
public class Archaea extends Organism implements Domain {

	public Archaea() {
		this.name = "Some Archaea";
		this.taxonomy.domain = this.getClass().getSimpleName();

		this.multicellular = false;
		this.reproduction = new String[] { "binary fission" };
		this.nutrition = new String[] { "decomposition" };
		this.locomotion = new String[] { "flagellar" };
	}

	@Override
	public void reproduce() {
		super.reproduce();
	}

}
