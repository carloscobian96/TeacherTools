package csi.cobian.organics;

import java.util.Arrays;

import csi.cobian.organics.taxonomy.Taxonomy;

public abstract class Organism {

	// Fields
	public String name;
	public Taxonomy taxonomy;

	public boolean multicellular;
	public String[] reproduction;
	public String[] nutrition;
	public String[] locomotion;

	// Constructors
	public Organism() {
		this.name = "An Organism";
		this.taxonomy = new Taxonomy();

		System.out.println("\n----------------------------------------");
		System.out.println("I'm a new " + this.getClass().getSimpleName() + ", glad to be alive!");

	}

	public Organism(String name, Taxonomy taxonomy) {
		this.name = name;
		this.taxonomy = taxonomy;
	}

	// Methods
	public void reproduce() {
		Arrays.stream(reproduction).forEach(r -> System.out.println(" 	Looking for some " + r + " ;)"));
	}

	public void requestFood() {
		Arrays.stream(nutrition).forEach(n -> System.out.println("	Give me " + n + " please!"));

	}

	public void eat() {
	}

	public String toString() {
		return String.format("""
				Name: %s
				Taxonomy: %s
				Nutrition: %s 
				Locomotion: %s 
				Reproduction: %s 
				""", 
				name, 
				taxonomy, 
				Arrays.toString(nutrition),
				Arrays.toString(locomotion),
				Arrays.toString(reproduction));
	}

}
