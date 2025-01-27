from tkinter import*
root = Tk()
root.title('PERIODIC_TABLE')
root.state('zoomed')
pt=Frame(root)
pt.grid(row=0,column=0)


#The information from the wikipedia is stored here
H_info='''Hydrogen is the chemical element with the symbol H and atomic number 1. With a standard atomic weight of 1.008, hydrogen is the lightest element in the periodic table. Hydrogen is the most abundant chemical substance in the Universe, constituting roughly 75% of all baryonic mass. Non-remnant stars are mainly composed of hydrogen in the plasma state. The most common isotope of hydrogen, termed protium (name rarely used, symbol 1H), has one proton and no neutrons.
The universal emergence of atomic hydrogen first occurred during the recombination epoch (Big Bang). At standard temperature and pressure, hydrogen is a colorless, odorless, tasteless, non-toxic, nonmetallic, highly combustible diatomic gas with the molecular formula H2. Since hydrogen readily forms covalent compounds with most nonmetallic elements, most of the hydrogen on Earth exists in molecular forms such as water or organic compounds. Hydrogen plays a particularly important role in acid–base reactions because most acid-base reactions involve the exchange of protons between soluble molecules. In ionic compounds, hydrogen can take the form of a negative charge (i.e., anion) when it is known as a hydride, or as a positively charged (i.e., cation) species denoted by the symbol H+. The hydrogen cation is written as though composed of a bare proton, but in reality, hydrogen cations in ionic compounds are always more complex. As the only neutral atom for which the Schrödinger equation can be solved analytically, study of the energetics and bonding of the hydrogen atom has played a key role in the development of quantum mechanics.
Hydrogen gas was first artificially produced in the early 16th century by the reaction of acids on metals. In 1766–81, Henry Cavendish was the first to recognize that hydrogen gas was a discrete substance, and that it produces water when burned, the property for which it was later named: in Greek, hydrogen means "water-former".
Industrial production is mainly from steam reforming natural gas, and less often from more energy-intensive methods such as the electrolysis of water. Most hydrogen is used near the site of its production, the two largest uses being fossil fuel processing (e.g., hydrocracking) and ammonia production, mostly for the fertilizer market. Hydrogen is problematic in metallurgy because it can embrittle many metals, complicating the design of pipelines and storage tanks.'''

He_info='''Helium (from Greek: ἥλιος, romanized: Helios, lit. 'Sun') is a chemical element with the symbol He and atomic number 2. It is a colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas group in the periodic table. Its boiling point is the lowest among all the elements. Helium is the second lightest and second most abundant element in the observable universe (hydrogen is the lightest and most abundant). It is present at about 24% of the total elemental mass, which is more than 12 times the mass of all the heavier elements combined. Its abundance is similar to this in both the Sun and in Jupiter. This is due to the very high nuclear binding energy (per nucleon) of helium-4, with respect to the next three elements after helium. This helium-4 binding energy also accounts for why it is a product of both nuclear fusion and radioactive decay. Most helium in the universe is helium-4, the vast majority of which was formed during the Big Bang. Large amounts of new helium are being created by nuclear fusion of hydrogen in stars.
Helium is named for the Greek Titan of the Sun, Helios. It was first detected as an unknown, yellow spectral line signature in sunlight, during a solar eclipse in 1868 by Georges Rayet, Captain C. T. Haig, Norman R. Pogson, and Lieutenant John Herschel, and was subsequently confirmed by French astronomer, Jules Janssen. Janssen is often jointly credited with detecting the element, along with Norman Lockyer. Janssen recorded the helium spectral line during the solar eclipse of 1868, while Lockyer observed it from Britain. Lockyer was the first to propose that the line was due to a new element, which he named. The formal discovery of the element was made in 1895 by two Swedish chemists, Per Teodor Cleve and Nils Abraham Langlet, who found helium emanating from the uranium ore, cleveite, which is now not regarded as a separate mineral species but as a variety of uraninite. In 1903, large reserves of helium were found in natural gas fields in parts of the United States, which is by far the largest supplier of the gas today.
Liquid helium is used in cryogenics (its largest single use, absorbing about a quarter of production), particularly in the cooling of superconducting magnets, with the main commercial application being in MRI scanners. Helium's other industrial uses—as a pressurizing and purge gas, as a protective atmosphere for arc welding and in processes such as growing crystals to make silicon wafers—account for half of the gas produced. A well-known but minor use is as a lifting gas in balloons and airships. As with any gas whose density differs from that of air, inhaling a small volume of helium temporarily changes the timbre and quality of the human voice. In scientific research, the behavior of the two fluid phases of helium-4 (helium I and helium II) is important to researchers studying quantum mechanics (in particular the property of superfluidity) and to those looking at the phenomena, such as superconductivity, produced in matter near absolute zero.
On Earth it is relatively rare—5.2 ppm by volume in the atmosphere. Most terrestrial helium present today is created by the natural radioactive decay of heavy radioactive elements (thorium and uranium, although there are other examples), as the alpha particles emitted by such decays consist of helium-4 nuclei. This radiogenic helium is trapped with natural gas in concentrations as great as 7% by volume, from which it is extracted commercially by a low-temperature separation process called fractional distillation. Previously, terrestrial helium—a non-renewable resource, because, once released into the atmosphere it readily escapes into space—was thought to be in increasingly short supply. However, recent studies suggest that helium produced deep in the earth by radioactive decay can collect in natural gas reserves in larger than expected quantities, in some cases, having been released by volcanic activity.'''

Li_info='''Lithium (from Greek: λίθος, romanized: lithos, lit. 'stone') is a chemical element with the symbol Li and atomic
number 3. It is a soft, silvery-white alkali metal. Under standard conditions, it is the lightest metal and the lightest
solid element. Like all alkali metals, lithium is highly reactive and flammable, and must be stored in mineral oil. When cut, it exhibits a metallic luster, but moist air corrodes it quickly to a dull silvery gray, then black tarnish. It never occurs freely in nature, but only in (usually ionic) compounds, such as pegmatitic minerals, which were once the main source of lithium. Due to its solubility as an ion, it is present in ocean water and is commonly obtained from brines. Lithium metal is isolated electrolytically from a mixture of lithium chloride and potassium chloride.
The nucleus of the lithium atom verges on instability, since the two stable lithium isotopes found in nature have among the lowest binding energies per nucleon of all stable nuclides. Because of its relative nuclear instability, lithium is less common in the solar system than 25 of the first 32 chemical elements even though its nuclei are very light: it is an exception to the trend that heavier nuclei are less common. For related reasons, lithium has important uses in nuclear physics. The transmutation of lithium atoms to helium in 1932 was the first fully man-made nuclear reaction, and lithium deuteride serves as a fusion fuel in staged thermonuclear weapons.Lithium and its compounds have several industrial applications, including heat-resistant glass and ceramics, lithium grease lubricants, flux additives for iron, steel and aluminium production, lithium batteries, and lithium-ion batteries. These uses consume more than three quarters of lithium production.
Lithium is present in biological systems in trace amounts; its functions are uncertain. Lithium salts have proven to be useful as a mood-stabilizing drug in the treatment of bipolar disorder in humans.'''

Be_info='''Beryllium is a chemical element with the symbol Be and atomic number 4. It is a relatively rare element in the universe, usually occurring as a product of the spallation of larger atomic nuclei that have collided with cosmic rays. Within the cores of stars, beryllium is depleted as it is fused into heavier elements. It is a divalent element which occurs naturally only in combination with other elements in minerals. Notable gemstones which contain beryllium include beryl (aquamarine, emerald) and chrysoberyl. As a free element it is a steel-gray, strong, lightweight and brittle alkaline earth metal.
In structural applications, the combination of high flexural rigidity, thermal stability, thermal conductivity and low density (1.85 times that of water) make beryllium metal a desirable aerospace material for aircraft components, missiles, spacecraft, and satellites. Because of its low density and atomic mass, beryllium is relatively transparent to X-rays and other forms of ionizing radiation; therefore, it is the most common window material for X-ray equipment and components of particle detectors. The high thermal conductivities of beryllium and beryllium oxide have led to their use in thermal management applications. When added as an alloying element to aluminium, copper (notably the alloy beryllium copper), iron or nickel beryllium improves many physical properties. Tools made of beryllium copper alloys are strong and hard and do not create sparks when they strike a steel surface. Beryllium does not form oxides until it reaches very high temperatures.
The commercial use of beryllium requires the use of appropriate dust control equipment and industrial controls at all times because of the toxicity of inhaled beryllium-containing dusts that can cause a chronic life-threatening allergic disease in some people ,called 'berylliosis'.'''

B_info='''Boron is a chemical element with the symbol B and atomic number 5. Produced entirely by cosmic ray spallation and supernovae and not by stellar nucleosynthesis, it is a low-abundance element in the Solar System and in the Earth's crust. Boron is concentrated on Earth by the water-solubility of its more common naturally occurring compounds, the borate minerals. These are mined industrially as evaporites, such as borax and kernite. The largest known boron deposits are in Turkey, the largest producer of boron minerals.
Elemental boron is a metalloid that is found in small amounts in meteoroids but chemically uncombined boron is not otherwise found naturally on Earth. Industrially, very pure boron is produced with difficulty because of refractory contamination by carbon or other elements. Several allotropes of boron exist: amorphous boron is a brown powder; crystalline boron is silvery to black, extremely hard (about 9.5 on the Mohs scale), and a poor electrical conductor at room temperature. The primary use of elemental boron is as boron filaments with applications similar to carbon fibers in some high-strength materials.
Boron is primarily used in chemical compounds. About half of all boron consumed globally is an additive in fiberglass for insulation and structural materials. The next leading use is in polymers and ceramics in high-strength, lightweight structural and refractory materials. Borosilicate glass is desired for its greater strength and thermal shock resistance than ordinary soda lime glass. Boron as sodium perborate is used as a bleach. A small amount of boron is used as a dopant in semiconductors, and reagent intermediates in the synthesis of organic fine chemicals. A few boron-containing organic pharmaceuticals are used or are in study. Natural boron is composed of two stable isotopes, one of which (boron-10) has a number of uses as a neutron-capturing agent.
In biology, borates have low toxicity in mammals (similar to table salt), but are more toxic to arthropods and are used as insecticides. Boric acid is mildly antimicrobial, and several natural boron-containing organic antibiotics are known. Boron is an essential plant nutrient and boron compounds such as borax and boric acid are used as fertilizers in agriculture, although it's only required in small amounts, with excess being toxic. Boron compounds play a strengthening role in the cell walls of all plants. There is no consensus on whether boron is an essential nutrient for mammals, including humans, although there is some evidence it supports bone health.'''

C_info='''Carbon (from Latin: carbo "coal") is a chemical element with the symbol C and atomic number 6. It is nonmetallic and tetravalent—making four electrons available to form covalent chemical bonds. It belongs to group 14 of the periodic table. Three isotopes occur naturally, 12C and 13C being stable, while 14C is a radionuclide, decaying with a half-life of about 5,730 years. Carbon is one of the few elements known since antiquity.Carbon is the 15th most abundant element in the Earth's crust, and the fourth most abundant element in the universe by mass after hydrogen, helium, and oxygen. Carbon's abundance, its unique diversity of organic compounds, and its unusual ability to form polymers at the temperatures commonly encountered on Earth enables this element to serve as a common element of all known life. It is the second most abundant element in the human body by mass (about 18.5%) after oxygen.The atoms of carbon can bond together in diverse ways, resulting in various allotropes of carbon. The best known allotropes are graphite, diamond, and buckminsterfullerene. The physical properties of carbon vary widely with the allotropic form. For example, graphite is opaque and black while diamond is highly transparent. Graphite is soft enough to form a streak on paper (hence its name, from the Greek verb "γράφειν" which means "to write"), while diamond is the hardest naturally occurring material known. Graphite is a good electrical conductor while diamond has a low electrical conductivity. Under normal conditions, diamond, carbon nanotubes, and graphene have the highest thermal conductivities of all known materials. All carbon allotropes are solids under normal conditions, with graphite being the most thermodynamically stable form at standard temperature and pressure. They are chemically resistant and require high temperature to react even with oxygen.
The most common oxidation state of carbon in inorganic compounds is +4, while +2 is found in carbon monoxide and transition metal carbonyl complexes. The largest sources of inorganic carbon are limestones, dolomites and carbon dioxide, but significant quantities occur in organic deposits of coal, peat, oil, and methane clathrates. Carbon forms a vast number of compounds, more than any other element, with almost ten million compounds described to date, and yet that number is but a fraction of the number of theoretically possible compounds under standard conditions. For this reason, carbon has often been referred to as the "king of the elements".'''

N_info='''Nitrogen is the chemical element with the symbol N and atomic number 7. It was first discovered and isolated by Scottish physician Daniel Rutherford in 1772. Although Carl Wilhelm Scheele and Henry Cavendish had independently done so at about the same time, Rutherford is generally accorded the credit because his work was published first. The name nitrogène was suggested by French chemist Jean-Antoine-Claude Chaptal in 1790, when it was found that nitrogen was present in nitric acid and nitrates. Antoine Lavoisier suggested instead the name azote, from the Greek ἀζωτικός "no life", as it is an asphyxiant gas; this name is instead used in many languages, such as French, Russian, Romanian and Turkish, and appears in the English names of some nitrogen compounds such as hydrazine, azides and azo compounds.
Nitrogen is the lightest member of group 15 of the periodic table, often called the pnictogens. The name comes from the Greek πνίγειν "to choke", directly referencing nitrogen's asphyxiating properties. It is a common element in the universe, estimated at about seventh in total abundance in the Milky Way and the Solar System. At standard temperature and pressure, two atoms of the element bind to form dinitrogen, a colourless and odorless diatomic gas with the formula N2. Dinitrogen forms about 78% of Earth's atmosphere, making it the most abundant uncombined element. Nitrogen occurs in all organisms, primarily in amino acids (and thus proteins), in the nucleic acids (DNA and RNA) and in the energy transfer molecule adenosine triphosphate. The human body contains about 3% nitrogen by mass, the fourth most abundant element in the body after oxygen, carbon, and hydrogen. The nitrogen cycle describes movement of the element from the air, into the biosphere and organic compounds, then back into the atmosphere.
Many industrially important compounds, such as ammonia, nitric acid, organic nitrates (propellants and explosives), and cyanides, contain nitrogen. The extremely strong triple bond in elemental nitrogen (N≡N), the second strongest bond in any diatomic molecule after carbon monoxide (CO), dominates nitrogen chemistry. This causes difficulty for both organisms and industry in converting N2 into useful compounds, but at the same time means that burning, exploding, or decomposing nitrogen compounds to form nitrogen gas releases large amounts of often useful energy. Synthetically produced ammonia and nitrates are key industrial fertilisers, and fertiliser nitrates are key pollutants in the eutrophication of water systems.
Apart from its use in fertilisers and energy-stores, nitrogen is a constituent of organic compounds as diverse as Kevlar used in high-strength fabric and cyanoacrylate used in superglue. Nitrogen is a constituent of every major pharmacological drug class, including antibiotics. Many drugs are mimics or prodrugs of natural nitrogen-containing signal molecules: for example, the organic nitrates nitroglycerin and nitroprusside control blood pressure by metabolizing into nitric oxide. Many notable nitrogen-containing drugs, such as the natural caffeine and morphine or the synthetic amphetamines, act on receptors of animal neurotransmitters.'''

O_info='''Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.8% of the Earth's atmosphere. As compounds including oxides, the element makes up almost half of the Earth's crust.Dioxygen provides the energy released in combustion and aerobic cellular respiration, and many major classes of organic molecules in living organisms contain oxygen atoms, such as proteins, nucleic acids, carbohydrates, and fats, as do the major constituent inorganic compounds of animal shells, teeth, and bone. Most of the mass of living organisms is oxygen as a component of water, the major constituent of lifeforms. Oxygen is continuously replenished in Earth's atmosphere by photosynthesis, which uses the energy of sunlight to produce oxygen from water and carbon dioxide. Oxygen is too chemically reactive to remain a free element in air without being continuously replenished by the photosynthetic action of living organisms. Another form (allotrope) of oxygen, ozone (O3), strongly absorbs ultraviolet UVB radiation and the high-altitude ozone layer helps protect the biosphere from ultraviolet radiation. However, ozone present at the surface is a byproduct of smog and thus a pollutant.
Oxygen was isolated by Michael Sendivogius before 1604, but it is commonly believed that the element was discovered independently by Carl Wilhelm Scheele, in Uppsala, in 1773 or earlier, and Joseph Priestley in Wiltshire, in 1774. Priority is often given for Priestley because his work was published first. Priestley, however, called oxygen "dephlogisticated air", and did not recognize it as a chemical element. The name oxygen was coined in 1777 by Antoine Lavoisier, who first recognized oxygen as a chemical element and correctly characterized the role it plays in combustion.
Common uses of oxygen include production of steel, plastics and textiles, brazing, welding and cutting of steels and other metals, rocket propellant, oxygen therapy, and life support systems in aircraft, submarines, spaceflight and diving.'''

F_info='''Fluoride () is an inorganic, monatomic anion with the chemical formula F− (also written [F]−), whose salts are typically white or colorless. Fluoride salts typically have distinctive bitter tastes, and are odorless. Its salts and minerals are important chemical reagents and industrial chemicals, mainly used in the production of hydrogen fluoride for fluorocarbons. Fluoride is classified as a weak base since it only partially associates in solution, but concentrated fluoride is corrosive and can attack the skin.
Fluoride is the simplest fluorine anion. In terms of charge and size, the fluoride ion resembles the hydroxide ion. Fluoride ions occur on earth in several minerals, particularly fluorite, but are present only in trace quantities in bodies of water in nature.
'''
Ne_info='''Neon is a chemical element with the symbol Ne and atomic number 10. It is a noble gas. Neon is a colorless, odorless, inert monatomic gas under standard conditions, with about two-thirds the density of air. It was discovered (along with krypton and xenon) in 1898 as one of the three residual rare inert elements remaining in dry air, after nitrogen, oxygen, argon and carbon dioxide were removed. Neon was the second of these three rare gases to be discovered and was immediately recognized as a new element from its bright red emission spectrum. The name neon is derived from the Greek word, νέον, neuter singular form of νέος (neos), meaning new. Neon is chemically inert, and no uncharged neon compounds are known. The compounds of neon currently known include ionic molecules, molecules held together by van der Waals forces and clathrates.
During cosmic nucleogenesis of the elements, large amounts of neon are built up from the alpha-capture fusion process in stars. Although neon is a very common element in the universe and solar system (it is fifth in cosmic abundance after hydrogen, helium, oxygen and carbon), it is rare on Earth. It composes about 18.2 ppm of air by volume (this is about the same as the molecular or mole fraction) and a smaller fraction in Earth's crust. The reason for neon's relative scarcity on Earth and the inner (terrestrial) planets is that neon is highly volatile and forms no compounds to fix it to solids. As a result, it escaped from the planetesimals under the warmth of the newly ignited Sun in the early Solar System. Even the outer atmosphere of Jupiter is somewhat depleted of neon, although for a different reason.Neon gives a distinct reddish-orange glow when used in low-voltage neon glow lamps, high-voltage discharge tubes and neon advertising signs. The red emission line from neon also causes the well known red light of helium–neon lasers. Neon is used in some plasma tube and refrigerant applications but has few other commercial uses. It is commercially extracted by the fractional distillation of liquid air. Since air is the only source, it is considerably more expensive than helium. '''

Na_info='''Sodium is a chemical element with the symbol Na (from Latin natrium) and atomic number 11. It is a soft, silvery-white, highly reactive metal. Sodium is an alkali metal, being in group 1 of the periodic table, because it has a single electron in its outer shell, which it readily donates, creating a positively charged ion—the Na+ cation. Its only stable isotope is 23Na. The free metal does not occur in nature, and must be prepared from compounds. Sodium is the sixth most abundant element in the Earth's crust and exists in numerous minerals such as feldspars, sodalite, and rock salt (NaCl). Many salts of sodium are highly water-soluble: sodium ions have been leached by the action of water from the Earth's minerals over eons, and thus sodium and chlorine are the most common dissolved elements by weight in the oceans.
Sodium was first isolated by Humphry Davy in 1807 by the electrolysis of sodium hydroxide. Among many other useful sodium compounds, sodium hydroxide (lye) is used in soap manufacture, and sodium chloride (edible salt) is a de-icing agent and a nutrient for animals including humans.
Sodium is an essential element for all animals and some plants. Sodium ions are the major cation in the extracellular fluid (ECF) and as such are the major contributor to the ECF osmotic pressure and ECF compartment volume. Loss of water from the ECF compartment increases the sodium concentration, a condition called hypernatremia. Isotonic loss of water and sodium from the ECF compartment decreases the size of that compartment in a condition called ECF hypovolemia.
By means of the sodium-potassium pump, living human cells pump three sodium ions out of the cell in exchange for two potassium ions pumped in; comparing ion concentrations across the cell membrane, inside to outside, potassium measures about 40:1, and sodium, about 1:10. In nerve cells, the electrical charge across the cell membrane enables transmission of the nerve impulse—an action potential—when the charge is dissipated; sodium plays a key role in that activity.'''

Mg_info='''Magnesium is a chemical element with the symbol Mg and atomic number 12. It is a shiny gray solid which bears a close physical resemblance to the other five elements in the second column (group 2, or alkaline earth metals) of the periodic table: all group 2 elements have the same electron configuration in the outer electron shell and a similar crystal structure.
Magnesium is the ninth most abundant element in the universe. It is produced in large, aging stars from the sequential addition of three helium nuclei to a carbon nucleus. When such stars explode as supernovas, much of the magnesium is expelled into the interstellar medium where it may recycle into new star systems. Magnesium is the eighth most abundant element in the Earth's crust and the fourth most common element in the Earth (after iron, oxygen and silicon), making up 13% of the planet's mass and a large fraction of the planet's mantle. It is the third most abundant element dissolved in seawater, after sodium and chlorine.Magnesium occurs naturally only in combination with other elements, where it invariably has a +2 oxidation state. The free element (metal) can be produced artificially, and is highly reactive (though in the atmosphere, it is soon coated in a thin layer of oxide that partly inhibits reactivity – see passivation). The free metal burns with a characteristic brilliant-white light. The metal is now obtained mainly by electrolysis of magnesium salts obtained from brine, and is used primarily as a component in aluminium-magnesium alloys, sometimes called magnalium or magnelium. Magnesium is less dense than aluminium, and the alloy is prized for its combination of lightness and strength.
Magnesium is the eleventh most abundant element by mass in the human body and is essential to all cells and some 300 enzymes. Magnesium ions interact with polyphosphate compounds such as ATP, DNA, and RNA. Hundreds of enzymes require magnesium ions to function. Magnesium compounds are used medicinally as common laxatives, antacids (e.g., milk of magnesia), and to stabilize abnormal nerve excitation or blood vessel spasm in such conditions as eclampsia.'''

Al_info='''Aluminium (aluminum in American and Canadian English) is a chemical element with the symbol Al and atomic number
13. It is a silvery-white, soft, non-magnetic and ductile metal in the boron group. By mass, aluminium makes up about 8% of
the Earth's crust, where it is the third most abundant element (after oxygen and silicon) and also the most abundant metal. Occurrence of aluminium decreases in the Earth's mantle below, however. The chief ore of aluminium is bauxite. Aluminium metal is highly reactive, such that native specimens are rare and limited to extreme reducing environments. Instead, it is found combined in over 270 different minerals.Aluminium is remarkable for its low density and its ability to resist corrosion through the phenomenon of passivation. Aluminium and its alloys are vital to the aerospace industry and important in transportation and building industries, such as building facades and window frames. The oxides and sulfates are the most useful compounds of aluminium.Despite its prevalence in the environment, no known form of life uses aluminium salts metabolically, but aluminium is well tolerated by plants and animals. Because of these salts' abundance, the potential for a biological role for them is of continuing interest, and studies continue. '''

Si_info='''Silicon is a chemical element with the symbol Si and atomic number 14. It is a hard, brittle crystalline solid with a blue-grey metallic lustre, and is a tetravalent metalloid and semiconductor. It is a member of group 14 in the periodic table: carbon is above it; and germanium, tin, and lead are below it. It is relatively unreactive. Because of its high chemical affinity for oxygen, it was not until 1823 that Jöns Jakob Berzelius was first able to prepare it and characterize it in pure form.  Its melting and boiling points of 1414 °C and 3265 °C respectively are the second-highest among all the metalloids and nonmetals, being only surpassed by boron. Silicon is the eighth most common element in the universe by mass, but very rarely occurs as the pure element in the Earth's crust. It is most widely distributed in dusts, sands, planetoids, and planets as various forms of silicon dioxide (silica) or silicates. More than 90% of the Earth's crust is composed of silicate minerals, making silicon the second most abundant element in the Earth's crust (about 28% by mass) after oxygen.
Most silicon is used commercially without being separated, and often with little processing of the natural minerals. Such use includes industrial construction with clays, silica sand, and stone. Silicates are used in Portland cement for mortar and stucco, and mixed with silica sand and gravel to make concrete for walkways, foundations, and roads. They are also used in whiteware ceramics such as porcelain, and in traditional quartz-based soda-lime glass and many other specialty glasses. Silicon compounds such as silicon carbide are used as abrasives and components of high-strength ceramics. Silicon is the basis of the widely used synthetic polymers called silicones.
The late 20th century to early 21st century has been described as the Silicon Age (also known as the Digital Age or Information Age) due to elemental silicon having a large impact on the modern world economy. The relatively small portion of very highly purified elemental silicon used in semiconductor electronics (< 10%) is essential to the metal–oxide–silicon (MOS) transistors and integrated circuit chips used in most modern technology (such as computers and cell phones, for example). The most widely used silicon device is the MOSFET (metal–oxide–silicon field-effect transistor), which has been manufactured in larger numbers than any other device in history. Free silicon is also used in the steel refining, aluminium-casting, and fine chemical industries (often to make fumed silica).
Silicon is an essential element in biology, although only traces are required by animals. However, various sea sponges and microorganisms, such as diatoms and radiolaria, secrete skeletal structures made of silica. Silica is deposited in many plant tissues.'''

P_info='''Phosphorus is a chemical element with the symbol P and atomic number 15. Elemental phosphorus exists in two major forms, white phosphorus and red phosphorus, but because it is highly reactive, phosphorus is never found as a free element on Earth. It has a concentration in the Earth's crust of about one gram per kilogram (compare copper at about 0.06 grams). In minerals, phosphorus generally occurs as phosphate.
Elemental phosphorus was first isolated as white phosphorus in 1669.  White phosphorus emits a faint glow when exposed to oxygen – hence the name, taken from Greek mythology, Φωσφόρος meaning "light-bearer" (Latin Lucifer), referring to the "Morning Star", the planet Venus. The term "phosphorescence", meaning glow after illumination, derives from this property of phosphorus, although the word has since been used for a diverse physical process that produces a glow. The glow of phosphorus is caused by oxidation of the white (but not red) phosphorus — a process now called chemiluminescence. Together with nitrogen, arsenic, antimony, and bismuth, phosphorus is classified as a pnictogen.
Phosphorus is essential for life. Phosphates (compounds containing the phosphate ion, PO43−) are a component of DNA, RNA, ATP, and phospholipids. Elemental phosphorus was first isolated from human urine, and bone ash was an important early phosphate source. Phosphate mines contain fossils because phosphate is present in the fossilized deposits of animal remains and excreta. Low phosphate levels are an important limit to growth in some aquatic systems. The vast majority of phosphorus compounds mined are consumed as fertilisers. Phosphate is needed to replace the phosphorus that plants remove from the soil, and its annual demand is rising nearly twice as fast as the growth of the human population. Other applications include organophosphorus compounds in detergents, pesticides, and nerve agents.'''

S_info='''Sulfur (in British English, sulphur) is a chemical element with the symbol S and atomic number 16. It is abundant, multivalent, and nonmetallic. Under normal conditions, sulfur atoms form cyclic octatomic molecules with a chemical formula S8. Elemental sulfur is a bright yellow, crystalline solid at room temperature.
Sulfur is the tenth most common element by mass in the universe, and the fifth most common on Earth. Though sometimes found in pure, native form, sulfur on Earth usually occurs as sulfide and sulfate minerals. Being abundant in native form, sulfur was known in ancient times, being mentioned for its uses in ancient India, ancient Greece, China, and Egypt. Historically and in literature sulfur is also called brimstone, which means "burning stone". Today, almost all elemental sulfur is produced as a byproduct of removing sulfur-containing contaminants from natural gas and petroleum. The greatest commercial use of the element is the production of sulfuric acid for sulfate and phosphate fertilizers, and other chemical processes. The element sulfur is used in matches, insecticides, and fungicides. Many sulfur compounds are odoriferous, and the smells of odorized natural gas, skunk scent, grapefruit, and garlic are due to organosulfur compounds. Hydrogen sulfide gives the characteristic odor to rotting eggs and other biological processes.
Sulfur is an essential element for all life, but almost always in the form of organosulfur compounds or metal sulfides. Three amino acids (cysteine, cystine, and methionine) and two vitamins (biotin and thiamine) are organosulfur compounds. Many cofactors also contain sulfur, including glutathione, thioredoxin, and iron–sulfur proteins. Disulfides, S–S bonds, confer mechanical strength and insolubility of the protein keratin, found in outer skin, hair, and feathers. Sulfur is one of the core chemical elements needed for biochemical functioning and is an elemental macronutrient for all living organisms.'''

Cl_info='''Chlorine is a chemical element with the symbol Cl and atomic number 17. The second-lightest of the halogens, it appears between fluorine and bromine in the periodic table and its properties are mostly intermediate between them. Chlorine is a yellow-green gas at room temperature. It is an extremely reactive element and a strong oxidising agent: among the elements, it has the highest electron affinity and the third-highest electronegativity on the Pauling scale, behind only oxygen and fluorine.
The most common compound of chlorine, sodium chloride (common salt), has been known since ancient times. Around 1630, chlorine gas was first synthesised in a chemical reaction, but not recognised as a fundamentally important substance. Carl Wilhelm Scheele wrote a description of chlorine gas in 1774, supposing it to be an oxide of a new element. In 1809, chemists suggested that the gas might be a pure element, and this was confirmed by Sir Humphry Davy in 1810, who named it from Ancient Greek: χλωρός, romanized: khlôros, lit. 'pale green' based on its colour.
Because of its great reactivity, all chlorine in the Earth's crust is in the form of ionic chloride compounds, which includes table salt. It is the second-most abundant halogen (after fluorine) and twenty-first most abundant chemical element in Earth's crust. These crustal deposits are nevertheless dwarfed by the huge reserves of chloride in seawater.
Elemental chlorine is commercially produced from brine by electrolysis, predominantly in the chlor-alkali process. The high oxidising potential of elemental chlorine led to the development of commercial bleaches and disinfectants, and a reagent for many processes in the chemical industry. Chlorine is used in the manufacture of a wide range of consumer products, about two-thirds of them organic chemicals such as polyvinyl chloride, and many intermediates for the production of plastics and other end products which do not contain the element. As a common disinfectant, elemental chlorine and chlorine-generating compounds are used more directly in swimming pools to keep them clean and sanitary. Elemental chlorine at high concentrations is extremely dangerous and poisonous for all living organisms, and was used in World War I as the first gaseous chemical warfare agent.
In the form of chloride ions, chlorine is necessary to all known species of life. Other types of chlorine compounds are rare in living organisms, and artificially produced chlorinated organics range from inert to toxic. In the upper atmosphere, chlorine-containing organic molecules such as chlorofluorocarbons have been implicated in ozone depletion. Small quantities of elemental chlorine are generated by oxidation of chloride to hypochlorite in neutrophils as part of the immune response against bacteria.'''

Ar_info='''Argon is a chemical element with the symbol Ar and atomic number 18. It is in group 18 of the periodic table and is a noble gas. Argon is the third-most abundant gas in the Earth's atmosphere, at 0.934% (9340 ppmv). It is more than twice as abundant as water vapor (which averages about 4000 ppmv, but varies greatly), 23 times as abundant as carbon dioxide (400 ppmv), and more than 500 times as abundant as neon (18 ppmv). Argon is the most abundant noble gas in Earth's crust, comprising 0.00015% of the crust.
Nearly all of the argon in the Earth's atmosphere is radiogenic argon-40, derived from the decay of potassium-40 in the Earth's crust. In the universe, argon-36 is by far the most common argon isotope, as it is the most easily produced by stellar nucleosynthesis in supernovas.
The name "argon" is derived from the Greek word ἀργόν, neuter singular form of ἀργός meaning "lazy" or "inactive", as a reference to the fact that the element undergoes almost no chemical reactions. The complete octet (eight electrons) in the outer atomic shell makes argon stable and resistant to bonding with other elements. Its triple point temperature of 83.8058 K is a defining fixed point in the International Temperature Scale of 1990.
Argon is produced industrially by the fractional distillation of liquid air. Argon is mostly used as an inert shielding gas in welding and other high-temperature industrial processes where ordinarily unreactive substances become reactive; for example, an argon atmosphere is used in graphite electric furnaces to prevent the graphite from burning. Argon is also used in incandescent, fluorescent lighting, and other gas-discharge tubes. Argon makes a distinctive blue-green gas laser. Argon is also used in fluorescent glow starters.'''

K_info='''Potassium is a chemical element with the symbol K (from Neo-Latin kalium) and atomic number 19. Potassium is a silvery-white metal that is soft enough to be cut with a knife with little force. Potassium metal reacts rapidly with atmospheric oxygen to form flaky white potassium peroxide in only seconds of exposure. It was first isolated from potash, the ashes of plants, from which its name derives. In the periodic table, potassium is one of the alkali metals, all of which have a single valence electron in the outer electron shell, that is easily removed to create an ion with a positive charge – a cation, that combines with anions to form salts. Potassium in nature occurs only in ionic salts. Elemental potassium reacts vigorously with water, generating sufficient heat to ignite hydrogen emitted in the reaction, and burning with a lilac-colored flame. It is found dissolved in sea water (which is 0.04% potassium by weight), and occurs in many minerals such as orthoclase, a common constituent of granites and other igneous rocks.
Potassium is chemically very similar to sodium, the previous element in group 1 of the periodic table. They have a similar first ionization energy, which allows for each atom to give up its sole outer electron. It was suspected in 1702 that they were distinct elements that combine with the same anions to make similar salts, and was proven in 1807 using electrolysis. Naturally occurring potassium is composed of three isotopes, of which 40K is radioactive. Traces of 40K are found in all potassium, and it is the most common radioisotope in the human body.
Potassium ions are vital for the functioning of all living cells. The transfer of potassium ions across nerve cell membranes is necessary for normal nerve transmission; potassium deficiency and excess can each result in numerous signs and symptoms, including an abnormal heart rhythm and various electrocardiographic abnormalities. Fresh fruits and vegetables are good dietary sources of potassium. The body responds to the influx of dietary potassium, which raises serum potassium levels, with a shift of potassium from outside to inside cells and an increase in potassium excretion by the kidneys.
Most industrial applications of potassium exploit the high solubility in water of potassium compounds, such as potassium soaps. Heavy crop production rapidly depletes the soil of potassium, and this can be remedied with agricultural fertilizers containing potassium, accounting for 95% of global potassium chemical production.'''

Ca_info='''Calcium is a chemical element with the symbol Ca and atomic number 20. As an alkaline earth metal, calcium is a reactive metal that forms a dark oxide-nitride layer when exposed to air. Its physical and chemical properties are most similar to its heavier homologues strontium and barium. It is the fifth most abundant element in Earth's crust and the third most abundant metal, after iron and aluminium. The most common calcium compound on Earth is calcium carbonate, found in limestone and the fossilised remnants of early sea life; gypsum, anhydrite, fluorite, and apatite are also sources of calcium. The name derives from Latin calx "lime", which was obtained from heating limestone.
Some calcium compounds were known to the ancients, though their chemistry was unknown until the seventeenth century. Pure calcium was isolated in 1808 via electrolysis of its oxide by Humphry Davy, who named the element. Calcium compounds are widely used in many industries: in foods and pharmaceuticals for calcium supplementation, in the paper industry as bleaches, as components in cement and electrical insulators, and in the manufacture of soaps. On the other hand, the metal in pure form has few applications due to its high reactivity; still, in small quantities it is often used as an alloying component in steelmaking, and sometimes, as a calcium–lead alloy, in making automotive batteries.
Calcium is the most abundant metal and the fifth-most abundant element in the human body. As electrolytes, calcium ions play a vital role in the physiological and biochemical processes of organisms and cells: in signal transduction pathways where they act as a second messenger; in neurotransmitter release from neurons; in contraction of all muscle cell types; as cofactors in many enzymes; and in fertilization. Calcium ions outside cells are important for maintaining the potential difference across excitable cell membranes, protein synthesis, and bone formation.'''

Sc_info='''Scandium is a chemical element with the symbol Sc and atomic number 21. A silvery-white metallic d-block element, it has historically been classified as a rare-earth element, together with yttrium and the lanthanides. It was discovered in 1879 by spectral analysis of the minerals euxenite and gadolinite from Scandinavia.
Scandium is present in most of the deposits of rare-earth and uranium compounds, but it is extracted from these ores in only a few mines worldwide. Because of the low availability and the difficulties in the preparation of metallic scandium, which was first done in 1937, applications for scandium were not developed until the 1970s, when the positive effects of scandium on aluminium alloys were discovered, and its use in such alloys remains its only major application. The global trade of scandium oxide is 15–20 tonnes per year.The properties of scandium compounds are intermediate between those of aluminium and yttrium. A diagonal relationship exists between the behavior of magnesium and scandium, just as there is between beryllium and aluminium. In the chemical compounds of the elements in group 3, the predominant oxidation state is +3.'''

Ti_info='''Titanium is a chemical element with the symbol Ti and atomic number 22. It is a lustrous transition metal with a silver color, low density, and high strength. Titanium is resistant to corrosion in sea water, aqua regia, and chlorine.
Titanium was discovered in Cornwall, Great Britain, by William Gregor in 1791 and was named by Martin Heinrich Klaproth after the Titans of Greek mythology. The element occurs within a number of mineral deposits, principally rutile and ilmenite, which are widely distributed in the Earth's crust and lithosphere; it is found in almost all living things, as well as bodies of water, rocks, and soils. The metal is extracted from its principal mineral ores by the Kroll and Hunter processes. The most common compound, titanium dioxide, is a popular photocatalyst and is used in the manufacture of white pigments. Other compounds include titanium tetrachloride (TiCl4), a component of smoke screens and catalysts; and titanium trichloride (TiCl3), which is used as a catalyst in the production of polypropylene.Titanium can be alloyed with iron, aluminium, vanadium, and molybdenum, among other elements, to produce strong, lightweight alloys for aerospace (jet engines, missiles, and spacecraft), military, industrial processes (chemicals and petrochemicals, desalination plants, pulp, and paper), automotive, agriculture (farming), medical prostheses, orthopedic implants, dental and endodontic instruments and files, dental implants, sporting goods, jewelry, mobile phones, and other applications.The two most useful properties of the metal are corrosion resistance and strength-to-density ratio, the highest of any metallic element. In its unalloyed condition, titanium is as strong as some steels, but less dense. There are two allotropic forms and five naturally occurring isotopes of this element, 46Ti through 50Ti, with 48Ti being the most abundant (73.8%). Although they have the same number of valence electrons and are in the same group in the periodic table, titanium and zirconium differ in many chemical and physical properties.'''

V_info='''Vanadium is a chemical element with the symbol V and atomic number 23. It is a hard, silvery-grey, malleable transition metal. The elemental metal is rarely found in nature, but once isolated artificially, the formation of an oxide layer (passivation) somewhat stabilizes the free metal against further oxidation.
Andrés Manuel del Río discovered compounds of vanadium in 1801 in Mexico by analyzing a new lead-bearing mineral he called "brown lead", and presumed its qualities were due to the presence of a new element, which he named erythronium (derived from the Greek word for "red", ἐρυθρόν, eruthrón) since upon heating most of the salts turned red. Four years later, he was (erroneously) convinced by other scientists that erythronium was identical to chromium. Chlorides of vanadium were generated in 1830 by Nils Gabriel Sefström who thereby proved that a new element was involved, which he named "vanadium" after the Scandinavian goddess of beauty and fertility, Vanadís (Freyja). Both names were attributed to the wide range of colors found in vanadium compounds. Del Rio's lead mineral was later renamed vanadinite for its vanadium content. In 1867 Henry Enfield Roscoe obtained the pure element.
Vanadium occurs naturally in about 65 minerals and in fossil fuel deposits. It is produced in China and Russia from steel smelter slag. Other countries produce it either from magnetite directly, flue dust of heavy oil, or as a byproduct of uranium mining. It is mainly used to produce specialty steel alloys such as high-speed tool steels. The most important industrial vanadium compound, vanadium pentoxide, is used as a catalyst for the production of sulfuric acid. The vanadium redox battery for energy storage may be an important application in the future.
Large amounts of vanadium ions are found in a few organisms, possibly as a toxin. The oxide and some other salts of vanadium have moderate toxicity. Particularly in the ocean, vanadium is used by some life forms as an active center of enzymes, such as the vanadium bromoperoxidase of some ocean algae.'''

Cr_info='''Chromium is a chemical element with the symbol Cr and atomic number 24. It is the first element in group 6. It is a steely-grey, lustrous, hard and brittle transition metal. Chromium is the main additive in stainless steel, to which it adds anti-corrosive properties. Chromium is also highly valued as a metal that is able to be highly polished while resisting tarnishing. Polished chromium reflects almost 70% of the visible spectrum, with almost 90% of infrared light being reflected. The name of the element is derived from the Greek word χρῶμα, chrōma, meaning color, because many chromium compounds are intensely colored.
Ferrochromium alloy is commercially produced from chromite by silicothermic or aluminothermic reactions and chromium metal by roasting and leaching processes followed by reduction with carbon and then aluminium. Chromium metal is of high value for its high corrosion resistance and hardness. A major development in steel production was the discovery that steel could be made highly resistant to corrosion and discoloration by adding metallic chromium to form stainless steel. Stainless steel and chrome plating (electroplating with chromium) together comprise 85% of the commercial use.
In the United States, trivalent chromium (Cr(III)) ion is considered an essential nutrient in humans for insulin, sugar and lipid metabolism. However, in 2014, the European Food Safety Authority, acting for the European Union, concluded that there was not sufficient evidence for chromium to be recognized as essential.While chromium metal and Cr(III) ions are not considered toxic, hexavalent chromium (Cr(VI)) is both toxic and carcinogenic. Abandoned chromium production sites often require environmental cleanup.'''

Mn_info='''Manganese is a chemical element with the symbol Mn and atomic number 25. It is found as a free element in nature; it is often found in minerals in combination with iron. Manganese is a transition metal with a multifaceted array of industrial alloy uses, particularly in stainless steels.
Historically, manganese is named for pyrolusite and other black minerals from the region of Magnesia in Greece, which also gave its name to magnesium and the iron ore magnetite. By the mid-18th century, Swedish-German chemist Carl Wilhelm Scheele had used pyrolusite to produce chlorine. Scheele and others were aware that pyrolusite (now known to be manganese dioxide) contained a new element, but they were unable to isolate it. Johan Gottlieb Gahn was the first to isolate an impure sample of manganese metal in 1774, which he did by reducing the dioxide with carbon.
Manganese phosphating is used for rust and corrosion prevention on steel. Ionized manganese is used industrially as pigments of various colors, which depend on the oxidation state of the ions. The permanganates of alkali and alkaline earth metals are powerful oxidizers. Manganese dioxide is used as the cathode (electron acceptor) material in zinc-carbon and alkaline batteries.
In biology, manganese(II) ions function as cofactors for a large variety of enzymes with many functions. Manganese enzymes are particularly essential in detoxification of superoxide free radicals in organisms that must deal with elemental oxygen. Manganese also functions in the oxygen-evolving complex of photosynthetic plants. While the element is a required trace mineral for all known living organisms, it also acts as a neurotoxin in larger amounts. Especially through inhalation, it can cause manganism, a condition in mammals leading to neurological damage that is sometimes irreversible.'''

Fe_info='''Iron is a chemical element with symbol Fe (from Latin: ferrum) and atomic number 26. It is a metal that belongs to the first transition series and group 8 of the periodic table. It is by mass the most common element on Earth, forming much of Earth's outer and inner core. It is the fourth most common element in the Earth's crust.
In its metallic state, iron is rare in the Earth's crust, limited to deposition by meteorites. Iron ores, by contrast, are among the most abundant in the Earth's crust, although extracting usable metal from them requires kilns or furnaces capable of reaching 1,500 °C (2,730 °F) or higher, about 500 °C (900 °F) higher than what is enough to smelt copper. Humans started to master that process in Eurasia only about 2000 BCE, and the use of iron tools and weapons began to displace copper alloys, in some regions, only around 1200 BCE. That event is considered the transition from the Bronze Age to the Iron Age. In the modern world, iron alloys, such as steel, inox, cast iron and special steels are by far the most common industrial metals, because of their mechanical properties and low cost.
Pristine and smooth pure iron surfaces are mirror-like silvery-gray. However, iron reacts readily with oxygen and water to give brown to black hydrated iron oxides, commonly known as rust. Unlike the oxides of some other metals, that form passivating layers, rust occupies more volume than the metal and thus flakes off, exposing fresh surfaces for corrosion.
The body of an adult human contains about 4 grams (0.005% body weight) of iron, mostly in hemoglobin and myoglobin. These two proteins play essential roles in vertebrate metabolism, respectively oxygen transport by blood and oxygen storage in muscles. To maintain the necessary levels, human iron metabolism requires a minimum of iron in the diet. Iron is also the metal at the active site of many important redox enzymes dealing with cellular respiration and oxidation and reduction in plants and animals.Chemically, the most common oxidation states of iron are iron(II) and iron(III). Iron shares many properties of other transition metals, including the other group 8 elements, ruthenium and osmium. Iron forms compounds in a wide range of oxidation states, −2 to +7. Iron also forms many coordination compounds; some of them, such as ferrocene, ferrioxalate, and Prussian blue, have substantial industrial, medical, or research applications.'''

Co_info='''Cobalt is a chemical element with the symbol Co and atomic number 27. Like nickel, cobalt is found in the Earth's crust only in chemically combined form, save for small deposits found in alloys of natural meteoric iron. The free element, produced by reductive smelting, is a hard, lustrous, silver-gray metal.
Cobalt-based blue pigments (cobalt blue) have been used since ancient times for jewelry and paints, and to impart a distinctive blue tint to glass, but the color was later thought to be due to the known metal bismuth. Miners had long used the name kobold ore (German for goblin ore) for some of the blue-pigment-producing minerals; they were so named because they were poor in known metals, and gave poisonous arsenic-containing fumes when smelted. In 1735, such ores were found to be reducible to a new metal (the first discovered since ancient times), and this was ultimately named for the kobold.
Today, some cobalt is produced specifically from one of a number of metallic-lustered ores, such as cobaltite (CoAsS). The element is, however, more usually produced as a by-product of copper and nickel mining. The copper belt in the Democratic Republic of the Congo (DRC) and Zambia yields most of the global cobalt production. World production in 2016 was 116,000 tonnes (according to Natural Resources Canada), and the DRC alone accounted for more than 50%.Cobalt is primarily used in lithium-ion batteries, and in the manufacture of magnetic, wear-resistant and high-strength alloys. The compounds cobalt silicate and cobalt(II) aluminate (CoAl2O4, cobalt blue) give a distinctive deep blue color to glass, ceramics, inks, paints and varnishes. Cobalt occurs naturally as only one stable isotope, cobalt-59. Cobalt-60 is a commercially important radioisotope, used as a radioactive tracer and for the production of high-energy gamma rays.
Cobalt is the active center of a group of coenzymes called cobalamins. Vitamin B12, the best-known example of the type, is an essential vitamin for all animals. Cobalt in inorganic form is also a micronutrient for bacteria, algae, and fungi.'''

Ni_info='''Nickel is a chemical element with the symbol Ni and atomic number 28. It is a silvery-white lustrous metal with a slight golden tinge. Nickel belongs to the transition metals and is hard and ductile. Pure nickel, powdered to maximize the reactive surface area, shows a significant chemical activity, but larger pieces are slow to react with air under standard conditions because an oxide layer forms on the surface and prevents further corrosion (passivation). Even so, pure native nickel is found in Earth's crust only in tiny amounts, usually in ultramafic rocks, and in the interiors of larger nickel–iron meteorites that were not exposed to oxygen when outside Earth's atmosphere.
Meteoric nickel is found in combination with iron, a reflection of the origin of those elements as major end products of supernova nucleosynthesis. An iron–nickel mixture is thought to compose Earth's outer and inner cores.Use of nickel (as a natural meteoric nickel–iron alloy) has been traced as far back as 3500 BCE. Nickel was first isolated and classified as a chemical element in 1751 by Axel Fredrik Cronstedt, who initially mistook the ore for a copper mineral, in the cobalt mines of Los, Hälsingland, Sweden. The element's name comes from a mischievous sprite of German miner mythology, Nickel (similar to Old Nick), who personified the fact that copper-nickel ores resisted refinement into copper. An economically important source of nickel is the iron ore limonite, which often contains 1–2% nickel. Nickel's other important ore minerals include pentlandite and a mixture of Ni-rich natural silicates known as garnierite. Major production sites include the Sudbury region in Canada (which is thought to be of meteoric origin), New Caledonia in the Pacific, and Norilsk in Russia.
Nickel is slowly oxidized by air at room temperature and is considered corrosion-resistant. Historically, it has been used for plating iron and brass, coating chemistry equipment, and manufacturing certain alloys that retain a high silvery polish, such as German silver. About 9% of world nickel production is still used for corrosion-resistant nickel plating. Nickel-plated objects sometimes provoke nickel allergy. Nickel has been widely used in coins, though its rising price has led to some replacement with cheaper metals in recent years.
Nickel is one of four elements (the others are iron, cobalt, and gadolinium) that are ferromagnetic at approximately room temperature. Alnico permanent magnets based partly on nickel are of intermediate strength between iron-based permanent magnets and rare-earth magnets. The metal is valuable in modern times chiefly in alloys; about 68% of world production is used in stainless steel. A further 10% is used for nickel-based and copper-based alloys, 7% for alloy steels, 3% in foundries, 9% in plating and 4% in other applications, including the fast-growing battery sector. As a compound, nickel has a number of niche chemical manufacturing uses, such as a catalyst for hydrogenation, cathodes for batteries, pigments and metal surface treatments. Nickel is an essential nutrient for some microorganisms and plants that have enzymes with nickel as an active site.
'''

Cu_info='''Copper is a chemical element with the symbol Cu (from Latin: cuprum) and atomic number 29. It is a soft, malleable, and ductile metal with very high thermal and electrical conductivity. A freshly exposed surface of pure copper has a pinkish-orange color. Copper is used as a conductor of heat and electricity, as a building material, and as a constituent of various metal alloys, such as sterling silver used in jewelry, cupronickel used to make marine hardware and coins, and constantan used in strain gauges and thermocouples for temperature measurement.
Copper is one of the few metals that can occur in nature in a directly usable metallic form (native metals). This led to very early human use in several regions, from c. 8000 BC. Thousands of years later, it was the first metal to be smelted from sulfide ores, c. 5000 BC; the first metal to be cast into a shape in a mold, c. 4000 BC; and the first metal to be purposefully alloyed with another metal, tin, to create bronze, c. 3500 BC.In the Roman era, copper was mined principally on Cyprus, the origin of the name of the metal, from aes сyprium (metal of Cyprus), later corrupted to сuprum (Latin). Coper (Old English) and copper were derived from this, the later spelling first used around 1530.Commonly encountered compounds are copper(II) salts, which often impart blue or green colors to such minerals as azurite, malachite, and turquoise, and have been used widely and historically as pigments.
Copper used in buildings, usually for roofing, oxidizes to form a green verdigris (or patina). Copper is sometimes used in decorative art, both in its elemental metal form and in compounds as pigments. Copper compounds are used as bacteriostatic agents, fungicides, and wood preservatives.
Copper is essential to all living organisms as a trace dietary mineral because it is a key constituent of the respiratory enzyme complex cytochrome c oxidase. In molluscs and crustaceans, copper is a constituent of the blood pigment hemocyanin, replaced by the iron-complexed hemoglobin in fish and other vertebrates. In humans, copper is found mainly in the liver, muscle, and bone. The adult body contains between 1.4 and 2.1 mg of copper per kilogram of body weight.'''

Zn_info='''Zinc is a chemical element with the symbol Zn and atomic number 30. Zinc is a slightly brittle metal at room temperature and has a blue-silvery appearance when oxidation is removed. It is the first element in group 12 of the periodic table. In some respects, zinc is chemically similar to magnesium: both elements exhibit only one normal oxidation state (+2), and the Zn2+ and Mg2+ ions are of similar size. Zinc is the 24th most abundant element in Earth's crust and has five stable isotopes. The most common zinc ore is sphalerite (zinc blende), a zinc sulfide mineral. The largest workable lodes are in Australia, Asia, and the United States. Zinc is refined by froth flotation of the ore, roasting, and final extraction using electricity (electrowinning).
Brass, an alloy of copper and zinc in various proportions, was used as early as the third millennium BC in the Aegean, Iraq, the United Arab Emirates, Kalmykia, Turkmenistan and Georgia, and the second millennium BC in West India, Uzbekistan, Iran, Syria, Iraq, and Israel/Palestine. Zinc metal was not produced on a large scale until the 12th century in India, though it was known to the ancient Romans and Greeks. The mines of Rajasthan have given definite evidence of zinc production going back to the 6th century BC. To date, the oldest evidence of pure zinc comes from Zawar, in Rajasthan, as early as the 9th century AD when a distillation process was employed to make pure zinc. Alchemists burned zinc in air to form what they called "philosopher's wool" or "white snow".
The element was probably named by the alchemist Paracelsus after the German word Zinke (prong, tooth). German chemist Andreas Sigismund Marggraf is credited with discovering pure metallic zinc in 1746. Work by Luigi Galvani and Alessandro Volta uncovered the electrochemical properties of zinc by 1800. Corrosion-resistant zinc plating of iron (hot-dip galvanizing) is the major application for zinc. Other applications are in electrical batteries, small non-structural castings, and alloys such as brass. A variety of zinc compounds are commonly used, such as zinc carbonate and zinc gluconate (as dietary supplements), zinc chloride (in deodorants), zinc pyrithione (anti-dandruff shampoos), zinc sulfide (in luminescent paints), and dimethylzinc or diethylzinc in the organic laboratory.
Zinc is an essential mineral, including to prenatal and postnatal development. Zinc deficiency affects about two billion people in the developing world and is associated with many diseases. In children, deficiency causes growth retardation, delayed sexual maturation, infection susceptibility, and diarrhea. Enzymes with a zinc atom in the reactive center are widespread in biochemistry, such as alcohol dehydrogenase in humans.Consumption of excess zinc may cause ataxia, lethargy, and copper deficiency.'''




Ga_info='''Gallium is a chemical element with the symbol Ga and atomic number 31. Elemental gallium is a soft, silvery blue metal at standard temperature and pressure; however in its liquid state it becomes silvery white. If too much force is applied, the gallium may fracture conchoidally. It is in group 13 of the periodic table, and thus has similarities to the other metals of the group, aluminium, indium, and thallium. Gallium does not occur as a free element in nature, but as gallium(III) compounds in trace amounts in zinc ores and in bauxite. Elemental gallium is a liquid at temperatures greater than 29.76 °C (85.57 °F), above room temperature, but below the normal human body temperature of 37 °C (99 °F). Hence, the metal will melt in a person's hands.
The melting point of gallium is used as a temperature reference point. Gallium alloys are used in thermometers as a non-toxic and environmentally friendly alternative to mercury, and can withstand higher temperatures than mercury. An even lower melting point of −19 °C (−2 °F), well below the freezing point of water, is claimed for the alloy galinstan (62–⁠95% gallium, 5–⁠22% indium, and 0–⁠16% tin by weight), but that may be the freezing point with the effect of supercooling.
Since its discovery in 1875, gallium has been used to make alloys with low melting points. It is also used in semiconductors as a dopant in semiconductor substrates.
Gallium is predominantly used in electronics. Gallium arsenide, the primary chemical compound of gallium in electronics, is used in microwave circuits, high-speed switching circuits, and infrared circuits. Semiconducting gallium nitride and indium gallium nitride produce blue and violet light-emitting diodes (LEDs) and diode lasers. Gallium is also used in the production of artificial gadolinium gallium garnet for jewelry. Gallium is considered a technology-critical element.
Gallium has no known natural role in biology. Gallium(III) behaves in a similar manner to ferric salts in biological systems and has been used in some medical applications, including pharmaceuticals and radiopharmaceuticals.'''

Ge_info='''Germanium is a chemical element with the symbol Ge and atomic number 32. It is a lustrous, hard-brittle, grayish-white metalloid in the carbon group, chemically similar to its group neighbours silicon and tin. Pure germanium is a semiconductor with an appearance similar to elemental silicon. Like silicon, germanium naturally reacts and forms complexes with oxygen in nature.
Because it seldom appears in high concentration, germanium was discovered comparatively late in the history of chemistry. Germanium ranks near fiftieth in relative abundance of the elements in the Earth's crust. In 1869, Dmitri Mendeleev predicted its existence and some of its properties from its position on his periodic table, and called the element ekasilicon. Nearly two decades later, in 1886, Clemens Winkler found the new element along with silver and sulfur, in a rare mineral called argyrodite. Although the new element somewhat resembled arsenic and antimony in appearance, the combining ratios in compounds agreed with Mendeleev's predictions for a relative of silicon. Winkler named the element after his country, Germany. Today, germanium is mined primarily from sphalerite (the primary ore of zinc), though germanium is also recovered commercially from silver, lead, and copper ores.
Elemental germanium is used as a semiconductor in transistors and various other electronic devices. Historically, the first decade of semiconductor electronics was based entirely on germanium. Presently, the major end uses are fibre-optic systems, infrared optics, solar cell applications, and light-emitting diodes (LEDs). Germanium compounds are also used for polymerization catalysts and have most recently found use in the production of nanowires. This element forms a large number of organogermanium compounds, such as tetraethylgermanium, useful in organometallic chemistry. Germanium is considered a technology-critical element.
Germanium is not thought to be an essential element for any living organism. Some complex organic germanium compounds are being investigated as possible pharmaceuticals, though none have yet proven successful. Similar to silicon and aluminium, natural germanium compounds tend to be insoluble in water and thus have little oral toxicity. However, synthetic soluble germanium salts are nephrotoxic, and synthetic chemically reactive germanium compounds with halogens and hydrogen are irritants and toxins.'''

As_info='''Arsenic is a chemical element with the symbol As and atomic number 33. Arsenic occurs in many minerals, usually in combination with sulfur and metals, but also as a pure elemental crystal. Arsenic is a metalloid. It has various allotropes, but only the gray form, which has a metallic appearance, is important to industry.
The primary use of arsenic is in alloys of lead (for example, in car batteries and ammunition). Arsenic is a common n-type dopant in semiconductor electronic devices, and the optoelectronic compound gallium arsenide is the second most commonly used semiconductor after doped silicon. Arsenic and its compounds, especially the trioxide, are used in the production of pesticides, treated wood products, herbicides, and insecticides. These applications are declining due to the toxicity of arsenic and its compounds.A few species of bacteria are able to use arsenic compounds as respiratory metabolites. Trace quantities of arsenic are an essential dietary element in rats, hamsters, goats, chickens, and presumably other species. A role in human metabolism is not known. However, arsenic poisoning occurs in multicellular life if quantities are larger than needed. Arsenic contamination of groundwater is a problem that affects millions of people across the world.
The United States' Environmental Protection Agency states that all forms of arsenic are a serious risk to human health. The United States' Agency for Toxic Substances and Disease Registry ranked arsenic as number 1 in its 2001 Priority List of Hazardous Substances at Superfund sites. Arsenic is classified as a Group-A carcinogen.
Selenium is a chemical element with the symbol Se and atomic number 34. It is a nonmetal (more rarely considered a metalloid) with properties that are intermediate between the elements above and below in the periodic table, sulfur and tellurium, and also has similarities to arsenic. It rarely occurs in its elemental state or as pure ore compounds in the Earth's crust. Selenium – from Ancient Greek σελήνη (selḗnē) "Moon" – was discovered in 1817 by Jöns Jacob Berzelius, who noted the similarity of the new element to the previously discovered tellurium (named for the Earth).
Selenium is found in metal sulfide ores, where it partially replaces the sulfur. Commercially, selenium is produced as a byproduct in the refining of these ores, most often during production. Minerals that are pure selenide or selenate compounds are known but rare. The chief commercial uses for selenium today are glassmaking and pigments. Selenium is a semiconductor and is used in photocells. Applications in electronics, once important, have been mostly replaced with silicon semiconductor devices. Selenium is still used in a few types of DC power surge protectors and one type of fluorescent quantum dot.'''

Se_info='''Selenium salts are toxic in large amounts, but trace amounts are necessary for cellular function in many organisms, including all animals. Selenium is an ingredient in many multivitamins and other dietary supplements, including infant formula. It is a component of the antioxidant enzymes glutathione peroxidase and thioredoxin reductase (which indirectly reduce certain oxidized molecules in animals and some plants). It is also found in three deiodinase enzymes, which convert one thyroid hormone to another. Selenium requirements in plants differ by species, with some plants requiring relatively large amounts and others apparently requiring none.'''

Br_info='''A bromide is a chemical compound containing a bromide ion or ligand. This is a bromine atom with an ionic charge of −1 (Br−); for example, in caesium bromide, caesium cations (Cs+) are electrically attracted to bromide anions (Br−) to form the electrically neutral ionic compound CsBr. The term "bromide" can also refer to a bromine atom with an oxidation number of −1 in covalent compounds such as sulfur dibromide (SBr2).'''

Kr_info='''Krypton (from Ancient Greek: κρυπτός, romanized: kryptos "the hidden one") is a chemical element with the symbol Kr and atomic number 36. It is a colorless, odorless, tasteless noble gas that occurs in trace amounts in the atmosphere and is often used with other rare gases in fluorescent lamps. With rare exceptions, krypton is chemically inert.
Krypton, like the other noble gases, is used in lighting and photography. Krypton light has many spectral lines, and krypton plasma is useful in bright, high-powered gas lasers (krypton ion and excimer lasers), each of which resonates and amplifies a single spectral line. Krypton fluoride also makes a useful laser medium. From 1960 to 1983, the official length of a meter was defined by the 606-nanometer wavelength of the orange spectral line of krypton-86, because of the high power and relative ease of operation of krypton discharge tubes.'''

Rb_info='''Rubidium is a chemical element with the symbol Rb and atomic number 37. Rubidium is a very soft, silvery-white metal in the alkali metal group. Rubidium metal shares similarities to potassium metal and caesium metal in physical appearance, softness and conductivity. Rubidium cannot be stored under atmospheric oxygen, as a highly exothermic reaction will ensue, sometimes even resulting in the metal catching fire.Rubidium is the first alkali metal in the group to have a density higher than water, so it sinks, unlike the metals above it in the group. Rubidium has a standard atomic weight of 85.4678. On Earth, natural rubidium comprises two isotopes: 72% is a stable isotope 85Rb, and 28% is slightly radioactive 87Rb, with a half-life of 49 billion years—more than three times as long as the estimated age of the universe.
German chemists Robert Bunsen and Gustav Kirchhoff discovered rubidium in 1861 by the newly developed technique, flame spectroscopy. The name comes from the Latin word rubidus, meaning deep red, the color of its emission spectrum. Rubidium's compounds have various chemical and electronic applications. Rubidium metal is easily vaporized and has a convenient spectral absorption range, making it a frequent target for laser manipulation of atoms. Rubidium is not a known nutrient for any living organisms. However, rubidium ions have the same charge as potassium ions and are actively taken up and treated by animal cells in similar ways.
Strontium is the chemical element with the symbol Sr and atomic number 38. An alkaline earth metal, strontium is a soft silver-white yellowish metallic element that is highly chemically reactive. The metal forms a dark oxide layer when it is exposed to air. Strontium has physical and chemical properties similar to those of its two vertical neighbors in the periodic table, calcium and barium. It occurs naturally mainly in the minerals celestine and strontianite, and is mostly mined from these. '''

Sr_info='''Both strontium and strontianite are named after Strontian, a village in Scotland near which the mineral was discovered in 1790 by Adair Crawford and William Cruickshank; it was identified as a new element the next year from its crimson-red flame test color. Strontium was first isolated as a metal in 1808 by Humphry Davy using the then newly-discovered process of electrolysis. During the 19th century, strontium was mostly used in the production of sugar from sugar beet (see strontian process). At the peak of production of television cathode ray tubes, as much as 75 percent of strontium consumption in the United States was used for the faceplate glass. With the replacement of cathode ray tubes with other display methods, consumption of strontium has dramatically declined.While natural strontium (which is mostly the isotope strontium-88) is stable, the synthetic strontium-90 is radioactive and is one of the most dangerous components of nuclear fallout, as strontium is absorbed by the body in a similar manner to calcium. Natural stable strontium, on the other hand, is not hazardous to health.'''

Y_info='''Yttrium is a chemical element with the symbol Y and atomic number 39. It is a silvery-metallic transition metal chemically similar to the lanthanides and has often been classified as a "rare-earth element". Yttrium is almost always found in combination with lanthanide elements in rare-earth minerals, and is never found in nature as a free element. 89Y is the only stable isotope, and the only isotope found in the Earth's crust.
The most important uses of yttrium are LEDs and phosphors, particularly the red phosphors in television set cathode ray tube displays. Yttrium is also used in the production of electrodes, electrolytes, electronic filters, lasers, superconductors, various medical applications, and tracing various materials to enhance their properties.
Yttrium has no known biological role. Exposure to yttrium compounds can cause lung disease in humans.The name is historical and comes from the village of Ytterby, in Sweden where, in 1787, the famous chemist Arrhenius found a new mineral and named it ytterbite.'''

Zr_info='''Zirconium is a chemical element with the symbol Zr and atomic number 40. The name zirconium is taken from the name of the mineral zircon (the word is related to Persian zargun (zircon; zar-gun, "gold-like" or "as gold")), the most important source of zirconium. It is a lustrous, grey-white, strong transition metal that closely resembles hafnium and, to a lesser extent, titanium. Zirconium is mainly used as a refractory and opacifier, although small amounts are used as an alloying agent for its strong resistance to corrosion. Zirconium forms a variety of inorganic and organometallic compounds such as zirconium dioxide and zirconocene dichloride, respectively. Five isotopes occur naturally, three of which are stable. Zirconium compounds have no known biological role.'''

Nb_info='''Niobium, also known as columbium, is a chemical element with the symbol Nb (formerly Cb) and atomic number 41. Niobium is a light grey, crystalline, and ductile transition metal. Pure niobium has a hardness similar to that of pure titanium, and it has similar ductility to iron. Niobium oxidizes in the earth's atmosphere very slowly, hence its application in jewelry as a hypoallergenic alternative to nickel. Niobium is often found in the minerals pyrochlore and columbite, hence the former name "columbium". Its name comes from Greek mythology, specifically Niobe, who was the daughter of Tantalus, the namesake of tantalum. The name reflects the great similarity between the two elements in their physical and chemical properties, making them difficult to distinguish.The English chemist Charles Hatchett reported a new element similar to tantalum in 1801 and named it columbium. In 1809, the English chemist William Hyde Wollaston wrongly concluded that tantalum and columbium were identical. The German chemist Heinrich Rose determined in 1846 that tantalum ores contain a second element, which he named niobium. In 1864 and 1865, a series of scientific findings clarified that niobium and columbium were the same element (as distinguished from tantalum), and for a century both names were used interchangeably. Niobium was officially adopted as the name of the element in 1949, but the name columbium remains in current use in metallurgy in the United States.
It was not until the early 20th century that niobium was first used commercially. Brazil is the leading producer of niobium and ferroniobium, an alloy of 60–70% niobium with iron. Niobium is used mostly in alloys, the largest part in special steel such as that used in gas pipelines. Although these alloys contain a maximum of 0.1%, the small percentage of niobium enhances the strength of the steel. The temperature stability of niobium-containing superalloys is important for its use in jet and rocket engines.
Niobium is used in various superconducting materials. These superconducting alloys, also containing titanium and tin, are widely used in the superconducting magnets of MRI scanners. Other applications of niobium include welding, nuclear industries, electronics, optics, numismatics, and jewelry. In the last two applications, the low toxicity and iridescence produced by anodization are highly desired properties. Niobium is considered a technology-critical element.
'''
Mo_info='''Molybdenum is a chemical element with the symbol Mo and atomic number 42. The name is from Neo-Latin molybdaenum, from Ancient Greek Μόλυβδος molybdos, meaning lead, since its ores were confused with lead ores. Molybdenum minerals have been known throughout history, but the element was discovered (in the sense of differentiating it as a new entity from the mineral salts of other metals) in 1778 by Carl Wilhelm Scheele. The metal was first isolated in 1781 by Peter Jacob Hjelm.Molybdenum does not occur naturally as a free metal on Earth; it is found only in various oxidation states in minerals. The free element, a silvery metal with a gray cast, has the sixth-highest melting point of any element. It readily forms hard, stable carbides in alloys, and for this reason most of world production of the element (about 80%) is used in steel alloys, including high-strength alloys and superalloys.
Most molybdenum compounds have low solubility in water, but when molybdenum-bearing minerals contact oxygen and water, the resulting molybdate ion MoO2−4 is quite soluble. Industrially, molybdenum compounds (about 14% of world production of the element) are used in high-pressure and high-temperature applications as pigments and catalysts.
Molybdenum-bearing enzymes are by far the most common bacterial catalysts for breaking the chemical bond in atmospheric molecular nitrogen in the process of biological nitrogen fixation. At least 50 molybdenum enzymes are now known in bacteria, plants, and animals, although only bacterial and cyanobacterial enzymes are involved in nitrogen fixation. These nitrogenases contain molybdenum in a form different from other molybdenum enzymes, which all contain fully oxidized molybdenum in a molybdenum cofactor. These various molybdenum cofactor enzymes are vital to the organisms, and molybdenum is an essential element for life in all higher eukaryote organisms, though not in all bacteria.'''

Tc_info='''Technetium is a chemical element with the symbol Tc and atomic number 43. It is the lightest element whose isotopes are all radioactive; none are stable other than the fully ionized state of 97Tc. Nearly all available technetium is produced as a synthetic element, and only about 18,000 tons are estimated to exist at any given time in the Earth's crust. Naturally occurring technetium is a spontaneous fission product in uranium ore and thorium ore, the most common source, or the product of neutron capture in molybdenum ores. This silvery gray, crystalline transition metal lies between manganese and rhenium in group 7 of the periodic table, and its chemical properties are intermediate between those of these two adjacent elements. The most common naturally occurring isotope is 99Tc.
Many of technetium's properties were predicted by Dmitri Mendeleev before the element was discovered. Mendeleev noted a gap in his periodic table and gave the undiscovered element the provisional name ekamanganese (Em). In 1937, technetium (specifically the technetium-97 isotope) became the first predominantly artificial element to be produced, hence its name (from the Greek τεχνητός, meaning "synthetic or artificial", + -ium).
One short-lived gamma ray-emitting nuclear isomer of technetium—technetium-99m—is used in nuclear medicine for a wide variety of diagnostic tests, such as bone cancer diagnoses. The ground state of this nuclide, technetium-99, is used as a gamma-ray-free source of beta particles. Long-lived technetium isotopes produced commercially are by-products of the fission of uranium-235 in nuclear reactors and are extracted from nuclear fuel rods. Because no isotope of technetium has a half-life longer than 4.21 million years (technetium-97), the 1952 detection of technetium in red giants helped to prove that stars can produce heavier elements.'''

Ru_info='''Ruthenium is a chemical element with the symbol Ru and atomic number 44. It is a rare transition metal belonging to the platinum group of the periodic table. Like the other metals of the platinum group, ruthenium is inert to most other chemicals. Russian-born scientist of Baltic-German ancestry Karl Ernst Claus discovered the element in 1844 at Kazan State University and named ruthenium in honor of Russia (Ruthenia is the Latin name of Rus). Ruthenium is usually found as a minor component of platinum ores; the annual production has risen from about 19 tonnes in 2009  to some 35.5 tonnes in 2017. Most ruthenium produced is used in wear-resistant electrical contacts and thick-film resistors. A minor application for ruthenium is in platinum alloys and as a chemistry catalyst. A new application of ruthenium is as the capping layer for extreme ultraviolet photomasks. Ruthenium is generally found in ores with the other platinum group metals in the Ural Mountains and in North and South America. Small but commercially important quantities are also found in pentlandite extracted from Sudbury, Ontario and in pyroxenite deposits in South Africa.
'''
Rh_info='''Rhodium is a chemical element with the symbol Rh and atomic number 45. It is a rare, silvery-white, hard, corrosion-resistant, and chemically inert transition metal. It is a noble metal and a member of the platinum group. It has only one naturally occurring isotope, 103Rh. Naturally occurring rhodium is usually found as free metal, as an alloy with similar metals, and rarely as a chemical compound in minerals such as bowieite and rhodplumsite. It is one of the rarest and most valuable precious metals.
Rhodium is found in platinum or nickel ores together with the other members of the platinum group metals. It was discovered in 1803 by William Hyde Wollaston in one such ore, and named for the rose color of one of its chlorine compounds.
The element's major use (approximately 80% of world rhodium production) is as one of the catalysts in the three-way catalytic converters in automobiles. Because rhodium metal is inert against corrosion and most aggressive chemicals, and because of its rarity, rhodium is usually alloyed with platinum or palladium and applied in high-temperature and corrosion-resistive coatings. White gold is often plated with a thin rhodium layer to improve its appearance while sterling silver is often rhodium-plated for tarnish resistance. Rhodium is sometimes used to cure silicones; a two-part silicone in which one part containing a silicon hydride and the other containing a vinyl-terminated silicone are mixed. One of these liquids contains a rhodium complex.Rhodium detectors are used in nuclear reactors to measure the neutron flux level. Other uses of rhodium include asymmetric hydrogenation used to form drug precursors and the processes for the production of acetic acid.'''

Pd_info='''Palladium is a chemical element with the symbol Pd and atomic number 46. It is a rare and lustrous silvery-white metal discovered in 1803 by the English chemist William Hyde Wollaston. He named it after the asteroid Pallas, which was itself named after the epithet of the Greek goddess Athena, acquired by her when she slew Pallas. Palladium, platinum, rhodium, ruthenium, iridium and osmium form a group of elements referred to as the platinum group metals (PGMs). They have similar chemical properties, but palladium has the lowest melting point and is the least dense of them.
More than half the supply of palladium and its congener platinum is used in catalytic converters, which convert as much as 90% of the harmful gases in automobile exhaust (hydrocarbons, carbon monoxide, and nitrogen dioxide) into less noxious substances (nitrogen, carbon dioxide and water vapor). Palladium is also used in electronics, dentistry, medicine, hydrogen purification, chemical applications, groundwater treatment, and jewelry. Palladium is a key component of fuel cells, which react hydrogen with oxygen to produce electricity, heat, and water.
Ore deposits of palladium and other PGMs are rare. The most extensive deposits have been found in the norite belt of the Bushveld Igneous Complex covering the Transvaal Basin in South Africa, the Stillwater Complex in Montana, United States; the Sudbury Basin and Thunder Bay District of Ontario, Canada, and the Norilsk Complex in Russia. Recycling is also a source, mostly from scrapped catalytic converters. The numerous applications and limited supply sources result in considerable investment interest.'''

Ag_info='''Silver is a chemical element with the symbol Ag (from the Latin argentum, derived from the Proto-Indo-European h₂erǵ: "shiny" or "white") and atomic number 47. A soft, white, lustrous transition metal, it exhibits the highest electrical conductivity, thermal conductivity, and reflectivity of any metal. The metal is found in the Earth's crust in the pure, free elemental form ("native silver"), as an alloy with gold and other metals, and in minerals such as argentite and chlorargyrite. Most silver is produced as a byproduct of copper, gold, lead, and zinc refining.
Silver has long been valued as a precious metal. Silver metal is used in many bullion coins, sometimes alongside gold: while it is more abundant than gold, it is much less abundant as a native metal. Its purity is typically measured on a per-mille basis; a 94%-pure alloy is described as "0.940 fine". As one of the seven metals of antiquity, silver has had an enduring role in most human cultures.
Other than in currency and as an investment medium (coins and bullion), silver is used in solar panels, water filtration, jewellery, ornaments, high-value tableware and utensils (hence the term silverware), in electrical contacts and conductors, in specialized mirrors, window coatings, in catalysis of chemical reactions, as a colorant in stained glass and in specialised confectionery. Its compounds are used in photographic and X-ray film. Dilute solutions of silver nitrate and other silver compounds are used as disinfectants and microbiocides (oligodynamic effect), added to bandages and wound-dressings, catheters, and other medical instruments.'''

Cd_info='''Cadmium is a chemical element with the symbol Cd and atomic number 48. This soft, silvery-white metal is chemically similar to the two other stable metals in group 12, zinc and mercury. Like zinc, it demonstrates oxidation state +2 in most of its compounds, and like mercury, it has a lower melting point than the transition metals in groups 3 through 11. Cadmium and its congeners in group 12 are often not considered transition metals, in that they do not have partly filled d or f electron shells in the elemental or common oxidation states. The average concentration of cadmium in Earth's crust is between 0.1 and 0.5 parts per million (ppm). It was discovered in 1817 simultaneously by Stromeyer and Hermann, both in Germany, as an impurity in zinc carbonate.
Cadmium occurs as a minor component in most zinc ores and is a byproduct of zinc production. Cadmium was used for a long time as a corrosion-resistant plating on steel, and cadmium compounds are used as red, orange and yellow pigments, to color glass, and to stabilize plastic. Cadmium use is generally decreasing because it is toxic (it is specifically listed in the European Restriction of Hazardous Substances) and nickel-cadmium batteries have been replaced with nickel-metal hydride and lithium-ion batteries. One of its few new uses is in cadmium telluride solar panels.
Although cadmium has no known biological function in higher organisms, a cadmium-dependent carbonic anhydrase has been found in marine diatoms.
'''
In_info='''Indium is a chemical element with the symbol In and atomic number 49. Indium is the softest metal that is not an alkali metal. It is a silvery-white metal that resembles tin in appearance. It is a post-transition metal that makes up 0.21 parts per million of the Earth's crust. Indium has a melting point higher than sodium and gallium, but lower than lithium and tin. Chemically, indium is similar to gallium and thallium, and it is largely intermediate between the two in terms of its properties. Indium was discovered in 1863 by Ferdinand Reich and Hieronymous Theodor Richter by spectroscopic methods. They named it for the indigo blue line in its spectrum. Indium was isolated the next year.
Indium is a minor component in zinc sulfide ores and is produced as a byproduct of zinc refinement. It is most notably used in the semiconductor industry, in low-melting-point metal alloys such as solders, in soft-metal high-vacuum seals, and in the production of transparent conductive coatings of indium tin oxide (ITO) on glass. Indium is considered a technology-critical element.
Indium has no biological role, though its compounds are toxic when injected into the bloodstream. Most occupational exposure is through ingestion, from which indium compounds are not absorbed well, and inhalation, from which they are moderately absorbed.
'''

Sn_info='''Tin is a chemical element with the symbol Sn (from Latin: stannum) and atomic number 50. Tin is a silvery metal that characteristically has a faint yellow hue. Tin, like indium, is soft enough to be cut without much force. When a bar of tin is bent, the so-called “tin cry” can be heard as a result of sliding tin crystals reforming; this trait is shared by indium, cadmium, and frozen mercury. Pure tin after solidifying keeps a mirror-like appearance similar to most metals. However, in most tin alloys (such as pewter), the metal solidifies with a dull gray color. Tin is a post-transition metal in group 14 of the periodic table of elements. It is obtained chiefly from the mineral cassiterite, which contains stannic oxide, SnO2. Tin shows a chemical similarity to both of its neighbors in group 14, germanium and lead, and has two main oxidation states, +2 and the slightly more stable +4. Tin is the 49th most abundant element on Earth and has, with 10 stable isotopes, the largest number of stable isotopes in the periodic table, thanks to its magic number of protons. It has two main allotropes: at room temperature, the stable allotrope is β-tin, a silvery-white, malleable metal, but at low temperatures, it transforms into the less dense grey α-tin, which has the diamond cubic structure. Metallic tin does not easily oxidize in air.
The first tin alloy used on a large scale was bronze, made of ​1⁄8 tin and ​7⁄8 copper, from as early as 3000 BC. After 600 BC, pure metallic tin was produced. Pewter, which is an alloy of 85–90% tin with the remainder commonly consisting of copper, antimony, and lead, was used for flatware from the Bronze Age until the 20th century. In modern times, tin is used in many alloys, most notably tin / lead soft solders, which are typically 60% or more tin, and in the manufacture of transparent, electrically conducting films of indium tin oxide in optoelectronic applications. Another large application for tin is corrosion-resistant tin plating of steel. Because of the low toxicity of inorganic tin, tin-plated steel is widely used for food packaging as tin cans. However, some organotin compounds can be almost as toxic as cyanide.
'''
Sb_info='''Antimony is a chemical element with the symbol Sb (from Latin: stibium) and atomic number 51. A lustrous gray metalloid, it is found in nature mainly as the sulfide mineral stibnite (Sb2S3). Antimony compounds have been known since ancient times and were powdered for use as medicine and cosmetics, often known by the Arabic name kohl. Metallic antimony was also known, but it was erroneously identified as lead upon its discovery. The earliest known description of the metal in the West was written in 1540 by Vannoccio Biringuccio.
For some time, China has been the largest producer of antimony and its compounds, with most production coming from the Xikuangshan Mine in Hunan. The industrial methods for refining antimony are roasting and reduction with carbon or direct reduction of stibnite with iron.
The largest applications for metallic antimony are an alloy with lead and tin and the lead antimony plates in lead–acid batteries. Alloys of lead and tin with antimony have improved properties for solders, bullets, and plain bearings. Antimony compounds are prominent additives for chlorine and bromine-containing fire retardants found in many commercial and domestic products. An emerging application is the use of antimony in microelectronics.'''

Te_info='''Tellurium is a chemical element with the symbol Te and atomic number 52. It is a brittle, mildly toxic, rare, silver-white metalloid. Tellurium is chemically related to selenium and sulfur, all three of which are chalcogens. It is occasionally found in native form as elemental crystals. Tellurium is far more common in the Universe as a whole than on Earth. Its extreme rarity in the Earth's crust, comparable to that of platinum, is due partly to its formation of a volatile hydride that caused tellurium to be lost to space as a gas during the hot nebular formation of Earth, and partly to tellurium's low affinity for oxygen, which causes it to bind preferentially to other chalcophiles in dense minerals that sink into the core.
Tellurium-bearing compounds were first discovered in 1782 in a gold mine in Kleinschlatten, Transylvania (now Zlatna, Romania) by Austrian mineralogist Franz-Joseph Müller von Reichenstein, although it was Martin Heinrich Klaproth who named the new element in 1798 after the Latin word for "earth", tellus. Gold telluride minerals are the most notable natural gold compounds. However, they are not a commercially significant source of tellurium itself, which is normally extracted as a by-product of copper and lead production.
Commercially, the primary use of tellurium is copper (tellurium copper) and steel alloys, where it improves machinability. Applications in CdTe solar panels and cadmium telluride semiconductors also consume a considerable portion of tellurium production. Tellurium is considered a technology-critical element.
Tellurium has no biological function, although fungi can use it in place of sulfur and selenium in amino acids such as tellurocysteine and telluromethionine. In humans, tellurium is partly metabolized into dimethyl telluride, (CH3)2Te, a gas with a garlic-like odor exhaled in the breath of victims of tellurium exposure or poisoning.
Iodine is a chemical element with the symbol I and atomic number 53. The heaviest of the stable halogens, it exists as a lustrous, purple-black non-metallic solid at standard conditions that melts to form a deep violet liquid at 114 degrees Celsius, and boils to a violet gas at 184 degrees Celsius. However, it sublimes easily with gentle heat, resulting in a widespread misconception even taught in some science textbooks that it does not melt. The element was discovered by the French chemist Bernard Courtois in 1811. It was named two years later by Joseph Louis Gay-Lussac, after the Greek ἰώδης "violet-coloured".'''

I_info='''Iodine occurs in many oxidation states, including iodide (I−), iodate (IO−3), and the various periodate anions. It is the least abundant of the stable halogens, being the sixty-first most abundant element. It is the heaviest essential mineral nutrient. Iodine is essential in the synthesis of thyroid hormones. Iodine deficiency affects about two billion people and is the leading preventable cause of intellectual disabilities.
The dominant producers of iodine today are Chile and Japan. Iodine and its compounds are primarily used in nutrition. Due to its high atomic number and ease of attachment to organic compounds, it has also found favour as a non-toxic radiocontrast material. Because of the specificity of its uptake by the human body, radioactive isotopes of iodine can also be used to treat thyroid cancer. Iodine is also used as a catalyst in the industrial production of acetic acid and some polymers.'''

Xe_info='''Xenon is a chemical element with the symbol Xe and atomic number 54. It is a colorless, dense, odorless noble gas found in Earth's atmosphere in trace amounts. Although generally unreactive, xenon can undergo a few chemical reactions such as the formation of xenon hexafluoroplatinate, the first noble gas compound to be synthesized.Xenon is used in flash lamps and arc lamps, and as a general anesthetic. The first excimer laser design used a xenon dimer molecule (Xe2) as the lasing medium, and the earliest laser designs used xenon flash lamps as pumps. Xenon is used to search for hypothetical weakly interacting massive particles and as the propellant for ion thrusters in spacecraft.Naturally occurring xenon consists of seven stable isotopes and two long-lived radioactive isotopes. More than 40 unstable xenon isotopes undergo radioactive decay, and the isotope ratios of xenon are an important tool for studying the early history of the Solar System. Radioactive xenon-135 is produced by beta decay from iodine-135 (a product of nuclear fission), and is the most significant (and unwanted) neutron absorber in nuclear reactors.'''

Cs_info='''Caesium (IUPAC spelling) (also spelled cesium in American English) is a chemical element with the symbol Cs and atomic number 55. It is a soft, silvery-golden alkali metal with a melting point of 28.5 °C (83.3 °F), which makes it one of only five elemental metals that are liquid at or near room temperature. Caesium has physical and chemical properties similar to those of rubidium and potassium. The most reactive of all metals, it is pyrophoric and reacts with water even at −116 °C (−177 °F). It is the least electronegative element, with a value of 0.79 on the Pauling scale. It has only one stable isotope, caesium-133. Caesium is mined mostly from pollucite, while the radioisotopes, especially caesium-137, a fission product, are extracted from waste produced by nuclear reactors.
The German chemist Robert Bunsen and physicist Gustav Kirchhoff discovered caesium in 1860 by the newly developed method of flame spectroscopy. The first small-scale applications for caesium were as a "getter" in vacuum tubes and in photoelectric cells. In 1967, acting on Einstein's proof that the speed of light is the most constant dimension in the universe, the International System of Units used two specific wave counts from an emission spectrum of caesium-133 to co-define the second and the metre. Since then, caesium has been widely used in highly accurate atomic clocks.
Since the 1990s, the largest application of the element has been as caesium formate for drilling fluids, but it has a range of applications in the production of electricity, in electronics, and in chemistry. The radioactive isotope caesium-137 has a half-life of about 30 years and is used in medical applications, industrial gauges, and hydrology. Nonradioactive caesium compounds are only mildly toxic, but the pure metal's tendency to react explosively with water means that caesium is considered a hazardous material, and the radioisotopes present a significant health and ecological hazard in the environment.'''

Ba_info='''Barium is a chemical element with the symbol Ba and atomic number 56. It is the fifth element in group 2 and is a soft, silvery alkaline earth metal. Because of its high chemical reactivity, barium is never found in nature as a free element. Its hydroxide, known in pre-modern times as baryta, does not occur as a mineral, but can be prepared by heating barium carbonate.
The most common naturally occurring minerals of barium are barite (now called baryte) (barium sulfate, BaSO4) and witherite (barium carbonate, BaCO3), both insoluble in water. The name barium originates from the alchemical derivative "baryta", from Greek βαρύς (barys), meaning "heavy". Baric is the adjectival form of barium. Barium was identified as a new element in 1774, but not reduced to a metal until 1808 with the advent of electrolysis.
Barium has few industrial applications. Historically, it was used as a getter for vacuum tubes and in oxide form as the emissive coating on indirectly heated cathodes. It is a component of YBCO (high-temperature superconductors) and electroceramics, and is added to steel and cast iron to reduce the size of carbon grains within the microstructure. Barium compounds are added to fireworks to impart a green color. Barium sulfate is used as an insoluble additive to oil well drilling fluid, as well as in a purer form, as X-ray radiocontrast agents for imaging the human gastrointestinal tract. The soluble barium ion and soluble compounds are poisonous, and have been used as rodenticides.
'''

La_info='''Lanthanum is a chemical element with the symbol La and atomic number 57. It is a soft, ductile, silvery-white metal that tarnishes slowly when exposed to air and is soft enough to be cut with a knife. It is the eponym of the lanthanide series, a group of 15 similar elements between lanthanum and lutetium in the periodic table, of which lanthanum is the first and the prototype. It is also sometimes considered the first element of the 6th-period transition metals, which would put it in group 3, although lutetium is sometimes placed in this position instead. Lanthanum is traditionally counted among the rare earth elements. The usual oxidation state is +3. Lanthanum has no biological role in humans but is essential to some bacteria. It is not particularly toxic to humans but does show some antimicrobial activity.
Lanthanum usually occurs together with cerium and the other rare earth elements. Lanthanum was first found by the Swedish chemist Carl Gustav Mosander in 1839 as an impurity in cerium nitrate – hence the name lanthanum, from the Ancient Greek λανθάνειν (lanthanein), meaning "to lie hidden". Although it is classified as a rare earth element, lanthanum is the 28th most abundant element in the Earth's crust, almost three times as abundant as lead. In minerals such as monazite and bastnäsite, lanthanum composes about a quarter of the lanthanide content. It is extracted from those minerals by a process of such complexity that pure lanthanum metal was not isolated until 1923.
Lanthanum compounds have numerous applications as catalysts, additives in glass, carbon arc lamps for studio lights and projectors, ignition elements in lighters and torches, electron cathodes, scintillators, GTAW electrodes, and other things. Lanthanum carbonate is used as a phosphate binder in cases of high levels of phosphate in the blood seen with kidney failure.'''

Ce_info='''Cerium is a chemical element with the symbol Ce and atomic number 58. Cerium is a soft, ductile and silvery-white metal that tarnishes when exposed to air, and it is soft enough to be cut with a knife. Cerium is the second element in the lanthanide series, and while it often shows the +3 oxidation state characteristic of the series, it also exceptionally has a stable +4 state that does not oxidize water. It is also considered one of the rare-earth elements. Cerium has no biological role in humans and is not very toxic.
Despite always occurring in combination with the other rare-earth elements in minerals such as those of the monazite and bastnäsite groups, cerium is easy to extract from its ores, as it can be distinguished among the lanthanides by its unique ability to be oxidized to the +4 state. It is the most common of the lanthanides, followed by neodymium, lanthanum, and praseodymium. It is the 26th-most abundant element, making up 66 ppm of the Earth's crust, half as much as chlorine and five times as much as lead.
Cerium was the first of the lanthanides to be discovered, in Bastnäs, Sweden, by Jöns Jakob Berzelius and Wilhelm Hisinger in 1803, and independently by Martin Heinrich Klaproth in Germany in the same year. In 1839 Carl Gustaf Mosander became the first to isolate the metal. Today, cerium and its compounds have a variety of uses: for example, cerium(IV) oxide is used to polish glass and is an important part of catalytic converters. Cerium metal is used in ferrocerium lighters for its pyrophoric properties. Cerium-doped YAG phosphor is used in conjunction with blue light-emitting diodes to produce white light in most commercial white LED light sources.'''

Pr_info='''Praseodymium is a chemical element with the symbol Pr and atomic number 59. It is the third member of the lanthanide series and is traditionally considered to be one of the rare-earth metals. Praseodymium is a soft, silvery, malleable and ductile metal, valued for its magnetic, electrical, chemical, and optical properties. It is too reactive to be found in native form, and pure praseodymium metal slowly develops a green oxide coating when exposed to air.  
Praseodymium always occurs naturally together with the other rare-earth metals. It is the fourth most common rare-earth element, making up 9.1 parts per million of the Earth's crust, an abundance similar to that of boron. In 1841, Swedish chemist Carl Gustav Mosander extracted a rare-earth oxide residue he called didymium from a residue he called "lanthana", in turn separated from cerium salts. In 1885, the Austrian chemist Baron Carl Auer von Welsbach separated didymium into two elements that gave salts of different colours, which he named praseodymium and neodymium. The name praseodymium comes from the Greek prasinos (πράσινος), meaning "green", and didymos (δίδυμος), "twin".
Like most rare-earth elements, praseodymium most readily forms the +3 oxidation state, which is the only stable state in aqueous solution, although the +4 oxidation state is known in some solid compounds and, uniquely among the lanthanides, the +5 oxidation state is attainable in matrix-isolation conditions. Aqueous praseodymium ions are yellowish-green, and similarly praseodymium results in various shades of yellow-green when incorporated into glasses. Many of praseodymium's industrial uses involve its ability to filter yellow light from light sources.
'''

Nd_info='''Neodymium is a chemical element with the symbol Nd and atomic number 60. Neodymium belongs to the lanthanide series and is a rare-earth element. It is a hard, slightly malleable silvery metal that quickly tarnishes in air and moisture. When oxidized, neodymium reacts quickly to produce pink, purple/blue and yellow compounds in the +2, +3 and +4 oxidation states. Neodymium was discovered in 1885 by the Austrian chemist Carl Auer von Welsbach. It is present in significant quantities in the ore minerals monazite and bastnäsite. Neodymium is not found naturally in metallic form or unmixed with other lanthanides, and it is usually refined for general use. Although neodymium is classed as a rare-earth element, it is fairly common, no rarer than cobalt, nickel, or copper, and is widely distributed in the Earth's crust. Most of the world's commercial neodymium is mined in China.
Neodymium compounds were first commercially used as glass dyes in 1927, and they remain a popular additive in glasses. The color of neodymium compounds is due to the Nd3+ ion and is often a reddish-purple, but it changes with the type of lighting, because of the interaction of the sharp light absorption bands of neodymium with ambient light enriched with the sharp visible emission bands of mercury, trivalent europium or terbium. Some neodymium-doped glasses are used in lasers that emit infrared with wavelengths between 1047 and 1062 nanometers. These have been used in extremely-high-power applications, such as experiments in inertial confinement fusion. Neodymium is also used with various other substrate crystals, such as yttrium aluminium garnet in the Nd:YAG laser. 
Another important use of neodymium is as a component in the alloys used to make high-strength neodymium magnets—powerful permanent magnets. These magnets are widely used in such products as microphones, professional loudspeakers, in-ear headphones, high performance hobby DC electric motors, and computer hard disks, where low magnet mass (or volume) or strong magnetic fields are required. Larger neodymium magnets are used in high-power-versus-weight electric motors (for example in hybrid cars) and generators (for example aircraft and wind turbine electric generators).
'''

Pm_info='''Promethium is a chemical element with the symbol Pm and atomic number 61. All of its isotopes are radioactive; it is extremely rare, with only about 500–600 grams naturally occurring in Earth's crust at any given time. Promethium is one of only two radioactive elements that are followed in the periodic table by elements with stable forms, the other being technetium. Chemically, promethium is a lanthanide. Promethium shows only one stable oxidation state of +3. 
In 1902 Bohuslav Brauner suggested that there was a then-unknown element with properties intermediate between those of the known elements neodymium (60) and samarium (62); this was confirmed in 1914 by Henry Moseley, who, having measured the atomic numbers of all the elements then known, found that atomic number 61 was missing. In 1926, two groups (one Italian and one American) claimed to have isolated a sample of element 61; both "discoveries" were soon proven to be false. In 1938, during a nuclear experiment conducted at Ohio State University, a few radioactive nuclides were produced that certainly were not radioisotopes of neodymium or samarium, but there was a lack of chemical proof that element 61 was produced, and the discovery was not generally recognized. Promethium was first produced and characterized at Oak Ridge National Laboratory in 1945 by the separation and analysis of the fission products of uranium fuel irradiated in a graphite reactor. The discoverers proposed the name "prometheum" (the spelling was subsequently changed), derived from Prometheus, the Titan in Greek mythology who stole fire from Mount Olympus and brought it down to humans, to symbolize "both the daring and the possible misuse of mankind's intellect". However, a sample of the metal was made only in 1963.
There are two possible sources for natural promethium: rare decays of natural europium-151 (producing promethium-147) and uranium (various isotopes). Practical applications exist only for chemical compounds of promethium-147, which are used in luminous paint, atomic batteries and thickness-measurement devices, even though promethium-145 is the most stable promethium isotope. Because natural promethium is exceedingly scarce, it is typically synthesized by bombarding uranium-235 (enriched uranium) with thermal neutrons to produce promethium-147 as a fission product.
'''
Sm_info='''Samarium is a chemical element with the symbol Sm and atomic number 62. It is a moderately hard silvery metal that slowly oxidizes in air. Being a typical member of the lanthanide series, samarium usually assumes the oxidation state +3. Compounds of samarium(II) are also known, most notably the monoxide SmO, monochalcogenides SmS, SmSe and SmTe, as well as samarium(II) iodide. The last compound is a common reducing agent in chemical synthesis. Samarium has no significant biological role but is only slightly toxic.
Samarium was discovered in 1879 by the French chemist Paul-Émile Lecoq de Boisbaudran and named after the mineral samarskite from which it was isolated. The mineral itself was earlier named after a Russian mine official, Colonel Vassili Samarsky-Bykhovets, who thereby became the first person to have a chemical element named after him, albeit indirectly. Although classified as a rare-earth element, samarium is the 40th most abundant element in the Earth's crust and is more common than metals such as tin. Samarium occurs with concentration up to 2.8% in several minerals including cerite, gadolinite, samarskite, monazite and bastnäsite, the last two being the most common commercial sources of the element. These minerals are mostly found in China, the United States, Brazil, India, Sri Lanka and Australia; China is by far the world leader in samarium mining and production.
The major commercial application of samarium is in samarium–cobalt magnets, which have permanent magnetization second only to neodymium magnets; however, samarium compounds can withstand significantly higher temperatures, above 700 °C (1,292 °F), without losing their magnetic properties, due to the alloy's higher Curie point. The radioactive isotope samarium-153 is the active component of the drug samarium (153Sm) lexidronam (Quadramet), which kills cancer cells in the treatment of lung cancer, prostate cancer, breast cancer and osteosarcoma. Another isotope, samarium-149, is a strong neutron absorber and is therefore added to the control rods of nuclear reactors. It is also formed as a decay product during the reactor operation and is one of the important factors considered in the reactor design and operation. Other applications of samarium include catalysis of chemical reactions, radioactive dating and X-ray lasers.
'''

Eu_info='''Europium is a chemical element with the symbol Eu and atomic number 63. Europium is the most reactive lanthanide by far, having to be stored under an inert fluid to protect it from atmospheric oxygen or moisture. Europium is also the softest lanthanide, as it can be dented with a fingernail and easily cut with a knife. When oxidation is removed a shiny-white metal is visible. Europium was isolated in 1901 and is named after the continent of Europe. Being a typical member of the lanthanide series, europium usually assumes the oxidation state +3, but the oxidation state +2 is also common. All europium compounds with oxidation state +2 are slightly reducing. Europium has no significant biological role and is relatively non-toxic compared to other heavy metals. Most applications of europium exploit the phosphorescence of europium compounds. Europium is one of the rarest of the rare earth elements on Earth.'''

Gd_info='''Gadolinium is a chemical element with the symbol Gd and atomic number 64. Gadolinium is a silvery-white metal when oxidation is removed. It is only slightly malleable and is a ductile rare-earth element. Gadolinium reacts with atmospheric oxygen or moisture slowly to form a black coating. Gadolinium below its Curie point of 20 °C (68 °F) is ferromagnetic, with an attraction to a magnetic field higher than that of nickel. Above this temperature it is the most paramagnetic element. It is found in nature only in an oxidized form. When separated, it usually has impurities of the other rare-earths because of their similar chemical properties.
Gadolinium was discovered in 1880 by Jean Charles de Marignac, who detected its oxide by using spectroscopy. It is named after the mineral gadolinite, one of the minerals in which gadolinium is found, itself named for the chemist Johan Gadolin. Pure gadolinium was first isolated by the chemist Paul Emile Lecoq de Boisbaudran around 1886.
Gadolinium possesses unusual metallurgical properties, to the extent that as little as 1% of gadolinium can significantly improve the workability and resistance to oxidation at high temperatures of iron, chromium, and related metals. Gadolinium as a metal or a salt absorbs neutrons and is, therefore, used sometimes for shielding in neutron radiography and in nuclear reactors.
Like most of the rare earths, gadolinium forms trivalent ions with fluorescent properties, and salts of gadolinium(III) are used as phosphors in various applications.
The kinds of gadolinium(III) ions occurring in water-soluble salts are toxic to mammals. However, chelated gadolinium(III) compounds are far less toxic because they carry gadolinium(III) through the kidneys and out of the body before the free ion can be released into the tissues. Because of its paramagnetic properties, solutions of chelated organic gadolinium complexes are used as intravenously administered gadolinium-based MRI contrast agents in medical magnetic resonance imaging.'''

Tb_info='''Terbium is a chemical element with the symbol Tb and atomic number 65. It is a silvery-white, rare earth metal that is malleable, ductile, and soft enough to be cut with a knife. The ninth member of the lanthanide series, terbium is a fairly electropositive metal that reacts with water, evolving hydrogen gas. Terbium is never found in nature as a free element, but it is contained in many minerals, including cerite, gadolinite, monazite, xenotime, and euxenite.
Swedish chemist Carl Gustaf Mosander discovered terbium as a chemical element in 1843. He detected it as an impurity in yttrium oxide, Y2O3. Yttrium and terbium are named after the village of Ytterby in Sweden. Terbium was not isolated in pure form until the advent of ion exchange techniques.
Terbium is used to dope calcium fluoride, calcium tungstate and strontium molybdate, materials that are used in solid-state devices, and as a crystal stabilizer of fuel cells which operate at elevated temperatures. As a component of Terfenol-D (an alloy that expands and contracts when exposed to magnetic fields more than any other alloy), terbium is of use in actuators, in naval sonar systems and in sensors.
Most of the world's terbium supply is used in green phosphors. Terbium oxide is in fluorescent lamps and television and monitor cathode ray tubes (CRTs). Terbium green phosphors are combined with divalent europium blue phosphors and trivalent europium red phosphors to provide trichromatic lighting technology, a high-efficiency white light used for standard illumination in indoor lighting.
'''
Dy_info='''Dysprosium is a chemical element with the symbol Dy and atomic number 66. It is a rare-earth element with a metallic silver luster. Dysprosium is never found in nature as a free element, though it is found in various minerals, such as xenotime. Naturally occurring dysprosium is composed of seven isotopes, the most abundant of which is 164Dy.
Dysprosium was first identified in 1886 by Paul Émile Lecoq de Boisbaudran, but it was not isolated in pure form until the development of ion-exchange techniques in the 1950s. Dysprosium has relatively few applications where it cannot be replaced by other chemical elements. It is used for its high thermal-neutron absorption cross-section in making control rods in nuclear reactors, for its high magnetic susceptibility (
  
    
      
        
          χ
          
            v
          
        
        ≈
        5.44
        ×
        
          10
          
            −
            3
          
        
      
    
    {\displaystyle \chi _{v}\approx 5.44\times 10^{-3}}
  ) in data-storage applications, and as a component of Terfenol-D (a magnetostrictive material). Soluble dysprosium salts
  are mildly toxic, while the insoluble salts are considered non-toxic.'''
Ho_info='''Holmium is a chemical element with the symbol Ho and atomic number 67. Part of the lanthanide series, holmium is a rare-earth element. 
Holmium was discovered through isolation by Swedish chemist Per Theodor Cleve and independently by Jacques-Louis Soret and Marc Delafontaine who observed it spectroscopically in 1878.
Its oxide was first isolated from rare-earth ores by Cleve in 1878. The element's name comes from Holmia, the Latin name for the city of Stockholm.Elemental holmium is a relatively soft and malleable silvery-white metal. It is too reactive to be found uncombined in nature, but when isolated, is relatively stable in dry air at room temperature. However, it reacts with water and corrodes readily and also burns in air when heated.
Holmium is found in the minerals monazite and gadolinite and is usually commercially extracted from monazite using ion-exchange techniques. Its compounds in nature and in nearly all of its laboratory chemistry are trivalently oxidized, containing Ho(III) ions. Trivalent holmium ions have fluorescent properties similar to many other rare-earth ions (while yielding their own set of unique emission light lines), and thus are used in the same way as some other rare earths in certain laser and glass-colorant applications.
Holmium has the highest magnetic permeability of any element and therefore is used for the polepieces of the strongest static magnets. Because holmium strongly absorbs neutrons, it is also used as a burnable poison in nuclear reactors.
'''
Er_info='''Erbium is a chemical element with the symbol Er and atomic number 68. A silvery-white solid metal when artificially isolated, natural erbium is always found in chemical combination with other elements. It is a lanthanide, a rare earth element, originally found in the gadolinite mine in Ytterby in Sweden, from which it got its name.
Erbium's principal uses involve its pink-colored Er3+ ions, which have optical fluorescent properties particularly useful in certain laser applications. Erbium-doped glasses or crystals can be used as optical amplification media, where Er3+ ions are optically pumped at around 980 or 1480 nm and then radiate light at 1530 nm in stimulated emission. This process results in an unusually mechanically simple laser optical amplifier for signals transmitted by fiber optics. The 1550 nm wavelength is especially important for optical communications because standard single mode optical fibers have minimal loss at this particular wavelength.
In addition to optical fiber amplifier-lasers, a large variety of medical applications (i.e. dermatology, dentistry) rely on the erbium ion's 2940 nm emission (see Er:YAG laser) when lit at another wavelength, which is highly absorbed in water in tissues, making its effect very superficial. Such shallow tissue deposition of laser energy is helpful in laser surgery, and for the efficient production of steam which produces enamel ablation by common types of dental laser.
'''
Tm_info='''Thulium is a chemical element with the symbol Tm and atomic number 69. It is the thirteenth and third-last element in the lanthanide series. Like the other lanthanides, the most common oxidation state is +3, seen in its oxide, halides and other compounds; because it occurs so late in the series, however, the +2 oxidation state is also stabilized by the nearly full 4f shell that results. In aqueous solution, like compounds of other late lanthanides, soluble thulium compounds form coordination complexes with nine water molecules.
In 1879, the Swedish chemist Per Teodor Cleve separated from the rare earth oxide erbia another two previously unknown components, which he called holmia and thulia; these were the oxides of holmium and thulium, respectively. A relatively pure sample of thulium metal was first obtained in 1911.
Thulium is the second-least abundant of the lanthanides, after radioactively unstable promethium which is only found in trace quantities on Earth. It is an easily workable metal with a bright silvery-gray luster. It is fairly soft and slowly tarnishes in air. Despite its high price and rarity, thulium is used as the radiation source in portable X-ray devices, and in some solid-state lasers. It has no significant biological role and is not particularly toxic.
'''

Yb_info='''Ytterbium is a chemical element with the symbol Yb and atomic number 70. It is the fourteenth and penultimate element in the lanthanide series, which is the basis of the relative stability of its +2 oxidation state. However, like the other lanthanides, its most common oxidation state is +3, as in its oxide, halides, and other compounds. In aqueous solution, like compounds of other late lanthanides, soluble ytterbium compounds form complexes with nine water molecules. Because of its closed-shell electron configuration, its density and melting and boiling points differ significantly from those of most other lanthanides.
In 1878, the Swiss chemist Jean Charles Galissard de Marignac separated from the rare earth "erbia" another independent component, which he called "ytterbia", for Ytterby, the village in Sweden near where he found the new component of erbium. He suspected that ytterbia was a compound of a new element that he called "ytterbium" (in total, four elements were named after the village, the others being yttrium, terbium and erbium). In 1907, the new earth "lutecia" was separated from ytterbia, from which the element "lutecium" (now lutetium) was extracted by Georges Urbain, Carl Auer von Welsbach, and Charles James. After some discussion, Marignac's name "ytterbium" was retained. A relatively pure sample of the metal was not obtained until 1953. At present, ytterbium is mainly used as a dopant of stainless steel or active laser media, and less often as a gamma ray source.
Natural ytterbium is a mixture of seven stable isotopes, which altogether are present at concentrations of 3 parts per million. This element is mined in China, the United States, Brazil, and India in form of the minerals monazite, euxenite, and xenotime. The ytterbium concentration is low because it is found only among many other rare earth elements; moreover, it is among the least abundant. Once extracted and prepared, ytterbium is somewhat hazardous as an eye and skin irritant. The metal is a fire and explosion hazard.
'''
Lu_info='''Lutetium is a chemical element with the symbol Lu and atomic number 71. It is a silvery white metal, which resists corrosion in dry air, but not in moist air. Lutetium is the last element in the lanthanide series, and it is traditionally counted among the rare earths. Lutetium is sometimes considered the first element of the 6th-period transition metals, although lanthanum is more often considered as such.
Lutetium was independently discovered in 1907 by French scientist Georges Urbain, Austrian mineralogist Baron Carl Auer von Welsbach, and American chemist Charles James. All of these researchers found lutetium as an impurity in the mineral ytterbia, which was previously thought to consist entirely of ytterbium. The dispute on the priority of the discovery occurred shortly after, with Urbain and Welsbach accusing each other of publishing results influenced by the published research of the other; the naming honor went to Urbain, as he had published his results earlier. He chose the name lutecium for the new element, but in 1949 the spelling of element 71 was changed to lutetium. In 1909, the priority was finally granted to Urbain and his names were adopted as official ones; however, the name cassiopeium (or later cassiopium) for element 71 proposed by Welsbach was used by many German scientists until the 1950s.
Lutetium is not a particularly abundant element, although it is significantly more common than silver in the earth's crust. It has few specific uses. Lutetium-176 is a relatively abundant (2.5%) radioactive isotope with a half-life of about 38 billion years, used to determine the age of minerals and meteorites. Lutetium usually occurs in association with the element yttrium and is sometimes used in metal alloys and as a catalyst in various chemical reactions. 177Lu-DOTA-TATE is used for radionuclide therapy (see Nuclear medicine) on neuroendocrine tumours. Lutetium has the highest Brinell hardness of any lanthanide, at 890–1300 MPa.
Hafnium is a chemical element with the symbol Hf and atomic number 72. A lustrous, silvery gray, tetravalent transition metal, hafnium chemically resembles zirconium and is found in many zirconium minerals. Its existence was predicted by Dmitri Mendeleev in 1869, though it was not identified until 1923, by Coster and Hevesy, making it the last stable element to be discovered. Hafnium is named after Hafnia, the Latin name for Copenhagen, where it was discovered.Hafnium is used in filaments and electrodes.  Some semiconductor fabrication processes use its oxide for integrated circuits at 45 nm and smaller feature lengths. Some superalloys used for special applications contain hafnium in combination with niobium, titanium, or tungsten.
'''
Hf_info='''Hafnium is a chemical element with the symbol Hf and atomic number 72. A lustrous, silvery gray, tetravalent transition metal, hafnium chemically resembles zirconium and is found in many zirconium minerals. Its existence was predicted by Dmitri Mendeleev in 1869, though it was not identified until 1923, by Coster and Hevesy, making it the last stable element to be discovered. Hafnium is named after Hafnia, the Latin name for Copenhagen, where it was discovered.Hafnium is used in filaments and electrodes.  Some semiconductor fabrication processes use its oxide for integrated circuits at 45 nm and smaller feature lengths. Some superalloys used for special applications contain hafnium in combination with niobium, titanium, or tungsten.
Hafnium's large neutron capture cross section makes it a good material for neutron absorption in control rods in nuclear power plants, but at the same time requires that it be removed from the neutron-transparent corrosion-resistant zirconium alloys used in nuclear reactors.'''

Ta_info='''Tantalum is a chemical element with the symbol Ta and atomic number 73. Previously known as tantalium, it is named after Tantalus, a villain from Greek mythology. Tantalum is a rare, hard, blue-gray, lustrous transition metal that is highly corrosion-resistant. It is part of the refractory metals group, which are widely used as minor components in alloys. The chemical inertness of tantalum makes it a valuable substance for laboratory equipment, and as a substitute for platinum. Its main use today is in tantalum capacitors in electronic equipment such as mobile phones, DVD players, video game systems and computers.
Tantalum, always together with the chemically similar niobium, occurs in the mineral groups tantalite, columbite and coltan (a mix of columbite and tantalite, though not recognised as a separate mineral species). Tantalum is considered a technology-critical element.
'''

W_info='''Tungsten, or wolfram, is a chemical element with the symbol W and atomic number 74. The name tungsten comes from the former Swedish name for the tungstate mineral scheelite, tungsten which means "heavy stone". Tungsten is a rare metal found naturally on Earth almost exclusively combined with other elements in chemical compounds rather than alone. It was identified as a new element in 1781 and first isolated as a metal in 1783. Its important ores include wolframite and scheelite.
The free element is remarkable for its robustness, especially the fact that it has the highest melting point of all the elements discovered, melting at 3,422 °C (6,192 °F; 3,695 K). It also has the highest boiling point, at 5,930 °C (10,710 °F; 6,200 K). Its density is 19.25 times that of water, comparable with that of uranium and gold, and much higher (about 1.7 times) than that of lead. Polycrystalline tungsten is an intrinsically brittle and hard material (under standard conditions, when uncombined), making it difficult to work. However, pure single-crystalline tungsten is more ductile and can be cut with a hard-steel hacksaw.Tungsten's many alloys have numerous applications, including incandescent light bulb filaments, X-ray tubes (as both the filament and target), electrodes in gas tungsten arc welding, superalloys, and radiation shielding. Tungsten's hardness and high density give it military applications in penetrating projectiles. Tungsten compounds are also often used as industrial catalysts.
Tungsten is the only metal from the third transition series that is known to occur in biomolecules that are found in a few species of bacteria and archaea. It is the heaviest element known to be essential to any living organism. However, tungsten interferes with molybdenum and copper metabolism and is somewhat toxic to more familiar forms of animal life.
'''
Re_info='''Rhenium is a chemical element with the symbol Re and atomic number 75. It is a silvery-gray, heavy, third-row transition metal in group 7 of the periodic table. With an estimated average concentration of 1 part per billion (ppb), rhenium is one of the rarest elements in the Earth's crust. Rhenium has the third-highest melting point and second-highest boiling point of any stable element at 5903 K. Rhenium resembles manganese and technetium chemically and is mainly obtained as a by-product of the extraction and refinement of molybdenum and copper ores. Rhenium shows in its compounds a wide variety of oxidation states ranging from −1 to +7.
Discovered in 1908, rhenium was the second-last stable element to be discovered (the last being hafnium). It was named after the river Rhine in Europe.
Nickel-based superalloys of rhenium are used in the combustion chambers, turbine blades, and exhaust nozzles of jet engines. These alloys contain up to 6% rhenium, making jet engine construction the largest single use for the element. The second-most important use is as a catalyst: rhenium is an excellent catalyst for hydrogenation and isomerization, and is used for example in catalytic reforming of naphtha for use in gasoline (rheniforming process). Because of the low availability relative to demand, rhenium is expensive, with price reaching an all-time high in 2008/2009 of US$10,600 per kilogram (US$4,800 per pound). Due to increases in rhenium recycling and a drop in demand for rhenium in catalysts, the price of rhenium has dropped to US$2,844 per kilogram (US$1,290 per pound) as of July 2018.
'''


Os_info='''Osmium (from Greek ὀσμή osme, "smell") is a chemical element with the symbol Os and atomic number 76. It is a hard, brittle, bluish-white transition metal in the platinum group that is found as a trace element in alloys, mostly in platinum ores. Osmium is the densest naturally occurring element, with an experimentally measured (using x-ray crystallography) density of 22.59 g/cm3. Manufacturers use its alloys with platinum, iridium, and other platinum-group metals to make fountain pen nib tipping, electrical contacts, and in other applications that require extreme durability and hardness. The element's abundance in the Earth's crust is among the rarest.
'''
Ir_info='''Iridium is a chemical element with the symbol Ir and atomic number 77. A very hard, brittle, silvery-white transition metal of the platinum group, iridium is considered to be the second-densest metal (after osmium) with a density of 22.56 g/cm3 as defined by experimental X-ray crystallography. However, at room temperature and standard atmospheric pressure, iridium has been calculated to have a density of 22.65 g/cm3, 0.04 g/cm3 higher than osmium measured the same way. Still, the experimental X-ray crystallography value is considered to be the most accurate, as such iridium is considered to be the second densest element. It is the most corrosion-resistant metal, even at temperatures as high as 2000 °C. Although only certain molten salts and halogens are corrosive to solid iridium, finely divided iridium dust is much more reactive and can be flammable.
Iridium was discovered in 1803 among insoluble impurities in natural platinum. Smithson Tennant, the primary discoverer, named iridium after the Greek goddess Iris, personification of the rainbow, because of the striking and diverse colors of its salts. Iridium is one of the rarest elements in Earth's crust, with annual production and consumption of only three tonnes. 191Ir and 193Ir are the only two naturally occurring isotopes of iridium, as well as the only stable isotopes; the latter is the more abundant.
The most important iridium compounds in use are the salts and acids it forms with chlorine, though iridium also forms a number of organometallic compounds used in industrial catalysis, and in research. Iridium metal is employed when high corrosion resistance at high temperatures is needed, as in high-performance spark plugs, crucibles for recrystallization of semiconductors at high temperatures, and electrodes for the production of chlorine in the chloralkali process. Iridium radioisotopes are used in some radioisotope thermoelectric generators.
Iridium is found in meteorites in much higher abundance than in the Earth's crust. For this reason, the unusually high abundance of iridium in the clay layer at the Cretaceous–Paleogene boundary gave rise to the Alvarez hypothesis that the impact of a massive extraterrestrial object caused the extinction of dinosaurs and many other species 66 million years ago. Similarly, an iridium anomaly in core samples from the Pacific Ocean suggested the Eltanin impact of about 2.5 million years ago.
It is thought that the total amount of iridium in the planet Earth is much higher than that observed in crystal rocks, but as with other platinum-group metals, the high density and tendency of iridium to bond with iron caused most iridium to descend below the crust when the planet was young and still molten.
'''

Pt_info='''Platinum is a chemical element with the symbol Pt and atomic number 78. It is a dense, malleable, ductile, highly unreactive, precious, silverish-white transition metal. Its name is derived from the Spanish term platino, meaning "little silver".Platinum is a member of the platinum group of elements and group 10 of the periodic table of elements. It has six naturally occurring isotopes. It is one of the rarer elements in Earth's crust, with an average abundance of approximately 5 μg/kg. It occurs in some nickel and copper ores along with some native deposits, mostly in South Africa, which accounts for 80% of the world production. Because of its scarcity in Earth's crust, only a few hundred tonnes are produced annually, and given its important uses, it is highly valuable and is a major precious metal commodity.Platinum is one of the least reactive metals. It has remarkable resistance to corrosion, even at high temperatures, and is therefore considered a noble metal. Consequently, platinum is often found chemically uncombined as native platinum. Because it occurs naturally in the alluvial sands of various rivers, it was first used by pre-Columbian South American natives to produce artifacts. It was referenced in European writings as early as 16th century, but it was not until Antonio de Ulloa published a report on a new metal of Colombian origin in 1748 that it began to be investigated by scientists.
Platinum is used in catalytic converters, laboratory equipment, electrical contacts and electrodes, platinum resistance thermometers, dentistry equipment, and jewelry. Being a heavy metal, it leads to health problems upon exposure to its salts; but due to its corrosion resistance, metallic platinum has not been linked to adverse health effects. Compounds containing platinum, such as cisplatin, oxaliplatin and carboplatin, are applied in chemotherapy against certain types of cancer.As of 2020, the value of platinum is around $32.00 per gram ($1,000 per troy ounce).
'''

Au_info='''Gold is a chemical element with the symbol Au (from Latin: aurum) and atomic number 79, making it one of the higher atomic number elements that occur naturally. In a pure form, it is a bright, slightly reddish yellow, dense, soft, malleable, and ductile metal. Chemically, gold is a transition metal and a group 11 element. It is one of the least reactive chemical elements and is solid under standard conditions. Gold often occurs in free elemental (native) form, as nuggets or grains, in rocks, in veins, and in alluvial deposits. It occurs in a solid solution series with the native element silver (as electrum) and also naturally alloyed with copper and palladium. Less commonly, it occurs in minerals as gold compounds, often with tellurium (gold tellurides).
Gold is resistant to most acids, though it does dissolve in aqua regia, a mixture of nitric acid and hydrochloric acid, which forms a soluble tetrachloroaurate anion. Gold is insoluble in nitric acid, which dissolves silver and base metals, a property that has long been used to refine gold and to confirm the presence of gold in metallic objects, giving rise to the term acid test. Gold also dissolves in alkaline solutions of cyanide, which are used in mining and electroplating. Gold dissolves in mercury, forming amalgam alloys, but this is not a chemical reaction.
A relatively rare element, gold is a precious metal that has been used as a neutron reflector in nuclear weapons (w71), and for coinage, jewelry, and other arts throughout recorded history. In the past, a gold standard was often implemented as a monetary policy, but gold coins ceased to be minted as a circulating currency in the 1930s, and the world gold standard was abandoned for a fiat currency system after 1971.
A total of 186,700 tonnes of gold exists above ground, as of 2015. The world consumption of new gold produced is about 50% in jewelry, 40% in investments, and 10% in industry. Gold's high malleability, ductility, resistance to corrosion and most other chemical reactions, and conductivity of electricity have led to its continued use in corrosion resistant electrical connectors in all types of computerized devices (its chief industrial use). Gold is also used in infrared shielding, colored-glass production, gold leafing, and tooth restoration. Certain gold salts are still used as anti-inflammatories in medicine. As of 2017, the world's largest gold producer by far was China with 440 tonnes per year.
'''

Hg_info='''Mercury is a chemical element with the symbol Hg and atomic number 80. It is commonly known as quicksilver and was formerly named hydrargyrum ( hy-DRAR-jər-əm). A heavy, silvery d-block element, mercury is the only metallic element that is liquid at standard conditions for temperature and pressure; the only other element that is liquid under these conditions is the halogen bromine, though metals such as caesium, gallium, and rubidium melt just above room temperature.
Mercury occurs in deposits throughout the world mostly as cinnabar (mercuric sulfide). The red pigment vermilion is obtained by grinding natural cinnabar or synthetic mercuric sulfide.
Mercury is used in thermometers, barometers, manometers, sphygmomanometers, float valves, mercury switches, mercury relays, fluorescent lamps and other devices, though concerns about the element's toxicity have led to mercury thermometers and sphygmomanometers being largely phased out in clinical environments in favor of alternatives such as alcohol- or galinstan-filled glass thermometers and thermistor- or infrared-based electronic instruments. Likewise, mechanical pressure gauges and electronic strain gauge sensors have replaced mercury sphygmomanometers.
Mercury remains in use in scientific research applications and in amalgam for dental restoration in some locales. It is also used in fluorescent lighting. Electricity passed through mercury vapor in a fluorescent lamp produces short-wave ultraviolet light, which then causes the phosphor in the tube to fluoresce, making visible light.
Mercury poisoning can result from exposure to water-soluble forms of mercury (such as mercuric chloride or methylmercury), by inhalation of mercury vapor, or by ingesting any form of mercury.
'''

Tl_info='''Thallium  is a chemical element with the symbol Tl and atomic number 81. It is a gray post-transition metal that is not found free in nature. When isolated, thallium resembles tin, but discolors when exposed to air. Chemists William Crookes and Claude-Auguste Lamy discovered thallium independently in 1861, in residues of sulfuric acid production. Both used the newly developed method of flame spectroscopy, in which thallium produces a notable green spectral line. Thallium, from Greek θαλλός, thallós, meaning "a green shoot or twig", was named by Crookes. It was isolated by both Lamy and Crookes in 1862; Lamy by electrolysis, and Crookes by precipitation and melting of the resultant powder. Crookes exhibited it as a powder precipitated by zinc at the International exhibition, which opened on 1 May that year.Thallium tends to form the +3 and +1 oxidation states. The +3 state resembles that of the other elements in group 13 (boron, aluminium, gallium, indium). However, the +1 state, which is far more prominent in thallium than the elements above it, recalls the chemistry of alkali metals, and thallium(I) ions are found geologically mostly in potassium-based ores, and (when ingested) are handled in many ways like potassium ions (K+) by ion pumps in living cells.
Commercially, thallium is produced not from potassium ores, but as a byproduct from refining of heavy-metal sulfide ores. Approximately 60–70% of thallium production is used in the electronics industry, and the remainder is used in the pharmaceutical industry and in glass manufacturing. It is also used in infrared detectors. The radioisotope thallium-201 (as the soluble chloride TlCl) is used in small amounts as an agent in a nuclear medicine scan, during one type of nuclear cardiac stress test.
Soluble thallium salts (many of which are nearly tasteless) are toxic, and they were historically used in rat poisons and insecticides. Use of these compounds has been restricted or banned in many countries, because of their nonselective toxicity. Thallium poisoning usually results in hair loss, although this characteristic symptom does not always surface. Because of its historic popularity as a murder weapon, thallium has gained notoriety as "the poisoner's poison" and "inheritance powder" (alongside arsenic).
'''
Pb_info='''Lead () is a chemical element with the symbol Pb (from the Latin plumbum) and atomic number 82. It is a heavy metal that is denser than most common materials. Lead is soft and malleable, and also has a relatively low melting point. When freshly cut, lead is silvery with a hint of blue; it tarnishes to a dull gray color when exposed to air. Lead has the highest atomic number of any stable element and three of its isotopes are endpoints of major nuclear decay chains of heavier elements.
Lead is a relatively unreactive post-transition metal. Its weak metallic character is illustrated by its amphoteric nature; lead and lead oxides react with acids and bases, and it tends to form covalent bonds. Compounds of lead are usually found in the +2 oxidation state rather than the +4 state common with lighter members of the carbon group. Exceptions are mostly limited to organolead compounds. Like the lighter members of the group, lead tends to bond with itself; it can form chains and polyhedral structures.
Lead is easily extracted from its ores; prehistoric people in Western Asia knew of it. Galena, a principal ore of lead, often bears silver, interest in which helped initiate widespread extraction and use of lead in ancient Rome. Lead production declined after the fall of Rome and did not reach comparable levels until the Industrial Revolution. In 2014, the annual global production of lead was about ten million tonnes, over half of which was from recycling. Lead's high density, low melting point, ductility and relative inertness to oxidation make it useful. These properties, combined with its relative abundance and low cost, resulted in its extensive use in construction, plumbing, batteries, bullets and shot, weights, solders, pewters, fusible alloys, white paints, leaded gasoline, and radiation shielding.
In the late 19th century, lead's toxicity was recognized, and its use has since been phased out of many applications. However, many countries still allow the sale of products that expose humans to lead, including some types of paints and bullets. Lead is a neurotoxin that accumulates in soft tissues and bones; it damages the nervous system and interferes with the function of biological enzymes, causing neurological disorders, such as brain damage and behavioral problems.
'''

Bi_info='''Bismuth is a chemical element with the symbol Bi and atomic number 83. It is a pentavalent post-transition metal and one of the pnictogens with chemical properties resembling its lighter homologs arsenic and antimony. Elemental bismuth may occur naturally, although its sulfide and oxide form important commercial ores. The free element is 86% as dense as lead. It is a brittle metal with a silvery white color when freshly produced, but surface oxidation can give it an iridescent tinge in numerous colours. Bismuth is the most naturally diamagnetic element, and has one of the lowest values of thermal conductivity among metals.
Bismuth was long considered the element with the highest atomic mass that is stable, but in 2003 it was discovered to be extremely weakly radioactive: its only primordial isotope, bismuth-209, decays via alpha decay with a half-life more than a billion times the estimated age of the universe. Because of its tremendously long half-life, bismuth may still be considered stable for almost all purposes.
'''
Po_info='''Polonium is a chemical element with the symbol Po and atomic number 84. A rare and highly radioactive metal with no stable isotopes, polonium is chemically similar to selenium and tellurium, though its metallic character resembles that of its horizontal neighbors in the periodic table: thallium, lead, and bismuth. Due to the short half-life of all its isotopes, its natural occurrence is limited to tiny traces of the fleeting polonium-210 (with a half-life of 138 days) in uranium ores, as it is the penultimate daughter of natural uranium-238. Though slightly longer-lived isotopes exist, they are much more difficult to produce. Today, polonium is usually produced in milligram quantities by the neutron irradiation of bismuth. Due to its intense radioactivity, which results in the radiolysis of chemical bonds and radioactive self-heating, its chemistry has mostly been investigated on the trace scale only.
Polonium was discovered in 1898 by Marie and Pierre Curie, when it was extracted from the uranium ore pitchblende and identified solely by its strong radioactivity: it was the first element to be so discovered. Polonium was named after Marie Curie's homeland of Poland. Polonium has few applications, and those are related to its radioactivity: heaters in space probes, antistatic devices, sources of neutrons and alpha particles, and poison. It is a radioactive element and extremely dangerous to humans.
'''

At_info='''Astatine is a radioactive chemical element with the symbol At and atomic number 85. It is the rarest naturally occurring element in the Earth's crust, occurring only as the decay product of various heavier elements. All of astatine's isotopes are short-lived; the most stable is astatine-210, with a half-life of 8.1 hours. A sample of the pure element has never been assembled, because any macroscopic specimen would be immediately vaporized by the heat of its own radioactivity.
The bulk properties of astatine are not known with any certainty. Many of them have been estimated based on the element's position on the periodic table as a heavier analog of iodine, and a member of the halogens (the group of elements including fluorine, chlorine, bromine, and iodine). Astatine is likely to have a dark or lustrous appearance and may be a semiconductor or possibly a metal; it probably has a higher melting point than that of iodine. Chemically, several anionic species of astatine are known and most of its compounds resemble those of iodine. It also shows some metallic behavior, including being able to form a stable monatomic cation in aqueous solution (unlike the lighter halogens).
The first synthesis of the element was in 1940 by Dale R. Corson, Kenneth Ross MacKenzie, and Emilio G. Segrè at the University of California, Berkeley, who named it from the Greek astatos (ἄστατος), meaning "unstable". Four isotopes of astatine were subsequently found to be naturally occurring, although much less than one gram is present at any given time in the Earth's crust. Neither the most stable isotope astatine-210, nor the medically useful astatine-211, occur naturally; they can only be produced synthetically, usually by bombarding bismuth-209 with alpha particles.
'''

Rn_info='''Radon is a chemical element with the symbol Rn and atomic number 86. It is a radioactive, colorless, odorless,
tasteless noble gas. It occurs naturally in minute quantities as an intermediate step in the normal radioactive decay chains
through which thorium and uranium slowly decay into lead and various other short-lived radioactive elements; radon itself
is the immediate decay product of radium. Its most stable isotope, 222Rn, has a half-life of only 3.8 days, making radon one of the rarest elements since it decays away so quickly. However, since thorium and uranium
are two of the most common radioactive elements on Earth, and they have three isotopes with very long half-lives, on the order of several billions of years, radon will be present on Earth long into the future in spite of its short half-life as it is continually being generated. The decay of radon produces many other short-lived nuclides known as radon daughters, ending at stable isotopes of lead.Unlike all the other intermediate elements in the aforementioned decay chains, radon is, under normal conditions, gaseous and easily inhaled. Radon gas is considered a health hazard. It is often the single largest contributor to an individual's background radiation dose, but due to local differences in geology, the level of the radon-gas hazard differs from location to location. Despite its short lifetime, radon gas from natural sources, such as uranium-containing minerals, can accumulate in buildings, especially, due to its high density, in low areas such as basements and crawl spaces. Radon can also occur in ground water – for example, in some spring waters and hot springs.Epidemiological studies have shown a clear link between breathing high concentrations of radon and incidence of lung cancer. Radon is a contaminant that affects indoor air quality worldwide. According to the United States Environmental Protection Agency (EPA), radon is the second most frequent cause of lung cancer, after cigarette smoking, causing 21,000 lung cancer deaths per year in the United States. About 2,900 of these deaths occur among people who have never smoked. While radon is the second most frequent cause of lung cancer, it is the number one cause among non-smokers, according to EPA policy-oriented estimates. Significant uncertainties exist for the health effects of low-dose exposures. Unlike the gaseous radon itself, radon
daughters are solids and stick to surfaces, such as airborne dust particles, which can cause lung cancer if inhaled.
'''
Fr_info='''Francium is a chemical element with the symbol Fr and atomic number 87. Prior to its discovery, it was referred to as eka-caesium. It is extremely radioactive; its most stable isotope, francium-223 (originally called actinium K after the natural decay chain it appears in), has a half-life of only 22 minutes. It is the second-most electropositive element, behind only caesium, and is the second rarest naturally occurring element (after astatine). The isotopes of francium decay quickly into astatine, radium, and radon. The electronic structure of a francium atom is [Rn] 7s1, and so the element is classed as an alkali metal.
Bulk francium has never been viewed. Because of the general appearance of the other elements in its periodic table column, it is assumed that francium would appear as a highly reactive metal, if enough could be collected together to be viewed as a bulk solid or liquid. Obtaining such a sample is highly improbable, since the extreme heat of decay caused by its short half-life would immediately vaporize any viewable quantity of the element.
Francium was discovered by Marguerite Perey in France (from which the element takes its name) in 1939. It was the last element first discovered in nature, rather than by synthesis. Outside the laboratory, francium is extremely rare, with trace amounts found in uranium and thorium ores, where the isotope francium-223 continually forms and decays. As little as 20–30 g (one ounce) exists at any given time throughout the Earth's crust; the other isotopes (except for francium-221) are entirely synthetic. The largest amount produced in the laboratory was a cluster of more than 300,000 atoms.
'''
Ra_info='''Radium is a chemical element with the symbol Ra and atomic number 88. It is the sixth element in group 2 of the periodic table, also known as the alkaline earth metals. Pure radium is silvery-white, but it readily reacts with nitrogen (rather than oxygen) on exposure to air, forming a black surface layer of radium nitride (Ra3N2). All isotopes of radium are highly radioactive, with the most stable isotope being radium-226, which has a half-life of 1600 years and decays into radon gas (specifically the isotope radon-222). When radium decays, ionizing radiation is a product, which can excite fluorescent chemicals and cause radioluminescence.
Radium, in the form of radium chloride, was discovered by Marie and Pierre Curie in 1898. They extracted the radium compound from uraninite and published the discovery at the French Academy of Sciences five days later. Radium was isolated in its metallic state by Marie Curie and André-Louis Debierne through the electrolysis of radium chloride in 1911.In nature, radium is found in uranium and (to a lesser extent) thorium ores in trace amounts as small as a seventh of a gram per ton of uraninite. Radium is not necessary for living organisms, and adverse health effects are likely when it is incorporated into biochemical processes because of its radioactivity and chemical reactivity. Currently, other than its use in nuclear medicine, radium has no commercial applications; formerly, it was used as a radioactive source for radioluminescent devices and also in radioactive quackery for its supposed curative powers. Today, these former applications are no longer in vogue because radium's toxicity has become known, and less dangerous isotopes are used instead in radioluminescent devices.
'''
Ac_info='''Actinium is a chemical element with the symbol Ac and atomic number 89. It was first isolated by French chemist André-Louis Debierne in 1899. Friedrich Oskar Giesel later independently isolated it in 1902 and, unaware that it was already known, gave it the name emanium. Actinium gave the name to the actinide series, a group of 15 similar elements between actinium and lawrencium in the periodic table. It is also sometimes considered the first of the 7th-period transition metals, although lawrencium is less commonly given that position. Together with polonium, radium, and radon, actinium was one of the first non-primordial radioactive elements to be isolated.
'''
Th_info='''Thorium is a weakly radioactive metallic chemical element with the symbol Th and atomic number 90. Thorium is silvery and tarnishes black when it is exposed to air, forming thorium dioxide; it is moderately hard, malleable, and has a high melting point. Thorium is an electropositive actinide whose chemistry is dominated by the +4 oxidation state; it is quite reactive and can ignite in air when finely divided.
All known thorium isotopes are unstable. The most stable isotope, 232Th, has a half-life of 14.05 billion years, or about the age of the universe; it decays very slowly via alpha decay, starting a decay chain named the thorium series that ends at stable 208Pb. On Earth, thorium, bismuth, and uranium are the only three radioactive elements that still occur naturally in large quantities as primordial elements. It is estimated to be over three times as abundant as uranium in the Earth's crust, and is chiefly refined from monazite sands as a by-product of extracting rare-earth metals.
Thorium was discovered in 1829 by the Norwegian amateur mineralogist Morten Thrane Esmark and identified by the Swedish chemist Jöns Jacob Berzelius, who named it after Thor, the Norse god of thunder. Its first applications were developed in the late 19th century. Thorium's radioactivity was widely acknowledged during the first decades of the 20th century. In the second half of the century, thorium was replaced in many uses due to concerns about its radioactivity.
Thorium is still being used as an alloying element in TIG welding electrodes but is slowly being replaced in the field with different compositions. It was also material in high-end optics and scientific instrumentation, used in some broadcast vacuum tubes, and as the light source in gas mantles, but these uses have become marginal. It has been suggested as a replacement for uranium as nuclear fuel in nuclear reactors, and several thorium reactors have been built.
'''

Pa_info='''Protactinium (formerly protoactinium) is a chemical element with the symbol Pa and atomic number 91. It is a dense, silvery-gray actinide metal which readily reacts with oxygen, water vapor and inorganic acids. It forms various chemical compounds in which protactinium is usually present in the oxidation state +5, but it can also assume +4 and even +3 or +2 states. Concentrations of protactinium in the Earth's crust are typically a few parts per trillion, but may reach up to a few parts per million in some uraninite ore deposits. Because of its scarcity, high radioactivity and high toxicity, there are currently no uses for protactinium outside scientific research, and for this purpose, protactinium is mostly extracted from spent nuclear fuel.
Protactinium was first identified in 1913 by Kasimir Fajans and Oswald Helmuth Göhring and named brevium because of the short half-life of the specific isotope studied, i.e. protactinium-234. A more stable isotope of protactinium, 231Pa, was discovered in 1917/18 by Otto Hahn and Lise Meitner, and they chose the name proto-actinium, but the IUPAC finally named it "protactinium" in 1949 and confirmed Hahn and Meitner as discoverers. The new name meant "(nuclear) precursor of actinium" and reflected that actinium is a product of radioactive decay of protactinium. John Arnold Cranston (working with Frederick Soddy and Ada Hitchins) is also credited with discovering the most stable isotope in 1915, but delayed his announcement due to being called up for service in the First World War.The longest-lived and most abundant (nearly 100%) naturally occurring isotope of protactinium, protactinium-231, has a half-life of 32,760 years and is a decay product of uranium-235. Much smaller trace amounts of the short-lived protactinium-234 and its nuclear isomer protactinium-234m occur in the decay chain of uranium-238. Protactinium-233 results from the decay of thorium-233 as part of the chain of events used to produce uranium-233 by neutron irradiation of thorium-232. It is an undesired intermediate product in thorium-based nuclear reactors and is therefore removed from the active zone of the reactor during the breeding process. Analysis of the relative concentrations of various uranium, thorium and protactinium isotopes in water and minerals is used in radiometric dating of sediments which are up to 175,000 years old and in modeling of various geological processes.
'''
U_info='''Uranium is a chemical element with the symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom has 92 protons and 92 electrons, of which 6 are valence electrons. Uranium is weakly radioactive because all isotopes of uranium are unstable; the half-lives of its naturally occurring isotopes range between 159,200 years and 4.5 billion years. The most common isotopes in natural uranium are uranium-238 (which has 146 neutrons and accounts for over 99% of uranium on Earth) and uranium-235 (which has 143 neutrons). Uranium has the highest atomic weight of the primordially occurring elements. Its density is about 70% higher than that of lead, and slightly lower than that of gold or tungsten. It occurs naturally in low concentrations of a few parts per million in soil, rock and water, and is commercially extracted from uranium-bearing minerals such as uraninite.In nature, uranium is found as uranium-238 (99.2739–99.2752%), uranium-235 (0.7198–0.7202%), and a very small amount of uranium-234 (0.0050–0.0059%). Uranium decays slowly by emitting an alpha particle. The half-life of uranium-238 is about 4.47 billion years and that of uranium-235 is 704 million years, making them useful in dating the age of the Earth.
Many contemporary uses of uranium exploit its unique nuclear properties. Uranium-235 is the only naturally occurring fissile isotope, which makes it widely used in nuclear power plants and nuclear weapons. However, because of the tiny amounts found in nature, uranium needs to undergo enrichment so that enough uranium-235 is present. Uranium-238 is fissionable by fast neutrons, and is fertile, meaning it can be transmuted to fissile plutonium-239 in a nuclear reactor. Another fissile isotope, uranium-233, can be produced from natural thorium and is also important in nuclear technology. Uranium-238 has a small probability for spontaneous fission or even induced fission with fast neutrons; uranium-235 and to a lesser degree uranium-233 have a much higher fission cross-section for slow neutrons. In sufficient concentration, these isotopes maintain a sustained nuclear chain reaction. This generates the heat in nuclear power reactors, and produces the fissile material for nuclear weapons. Depleted uranium (238U) is used in kinetic energy penetrators and armor plating. Uranium is used as a colorant in uranium glass, producing lemon yellow to green colors. Uranium glass fluoresces green in ultraviolet light. It was also used for tinting and shading in early photography.
The 1789 discovery of uranium in the mineral pitchblende is credited to Martin Heinrich Klaproth, who named the new element after the recently discovered planet Uranus. Eugène-Melchior Péligot was the first person to isolate the metal and its radioactive properties were discovered in 1896 by Henri Becquerel. Research by Otto Hahn, Lise Meitner, Enrico Fermi and others, such as J. Robert Oppenheimer starting in 1934 led to its use as a fuel in the nuclear power industry and in Little Boy, the first nuclear weapon used in war. An ensuing arms race during the Cold War between the United States and the Soviet Union produced tens of thousands of nuclear weapons that used uranium metal and uranium-derived plutonium-239. The security of those weapons and their fissile material following the breakup of the Soviet Union in 1991 is an ongoing concern for public health and safety. See Nuclear proliferation.
'''

Np_info='''Neptunium is a chemical element with the symbol Np and atomic number 93. A radioactive actinide metal, neptunium is the first transuranic element. Its position in the periodic table just after uranium, named after the planet Uranus, led to it being named after Neptune, the next planet beyond Uranus. A neptunium atom has 93 protons and 93 electrons, of which seven are valence electrons. Neptunium metal is silvery and tarnishes when exposed to air. The element occurs in three allotropic forms and it normally exhibits five oxidation states, ranging from +3 to +7. It is radioactive, poisonous, pyrophoric, and capable of accumulating in bones, which makes the handling of neptunium dangerous.
Although many false claims of its discovery were made over the years, the element was first synthesized by Edwin McMillan and Philip H. Abelson at the Berkeley Radiation Laboratory in 1940. Since then, most neptunium has been and still is produced by neutron irradiation of uranium in nuclear reactors. The vast majority is generated as a by-product in conventional nuclear power reactors. While neptunium itself has no commercial uses at present, it is used as a precursor for the formation of plutonium-238, used in radioisotope thermal generators to provide electricity for spacecraft. Neptunium has also been used in detectors of high-energy neutrons.
The longest-lived isotope of neptunium, neptunium-237, is a by-product of nuclear reactors and plutonium production. It, and the isotope neptunium-239, are also found in trace amounts in uranium ores due to neutron capture reactions and beta decay.
'''
Pu_info='''Plutonium is a radioactive chemical element with the symbol Pu and atomic number 94. It is an actinide metal of silvery-gray appearance that tarnishes when exposed to air, and forms a dull coating when oxidized. The element normally exhibits six allotropes and four oxidation states. It reacts with carbon, halogens, nitrogen, silicon, and hydrogen. When exposed to moist air, it forms oxides and hydrides that can expand the sample up to 70% in volume, which in turn flake off as a powder that is pyrophoric. It is radioactive and can accumulate in bones, which makes the handling of plutonium dangerous.
Plutonium was first produced and isolated on December 14, 1940, by a deuteron bombardment of uranium-238 in the 1.5 metre (60 in) cyclotron at the University of California, Berkeley. First, neptunium-238 (half-life 2.1 days) was synthesized, which subsequently beta-decayed to form the new element with atomic number 94 and atomic weight 238 (half-life 88 years). Since uranium had been named after the planet Uranus and neptunium after the planet Neptune, element 94 was named after Pluto, which at the time was considered to be a planet as well. Wartime secrecy prevented the University of California team from publishing its discovery until 1948. 
Plutonium is the element with the highest atomic number to occur in nature. Trace quantities arise in natural uranium-238 deposits when uranium-238 captures neutrons emitted by decay of other uranium-238 atoms. Plutonium is much more common on Earth since 1945 as a product of neutron capture and beta decay, where some of the neutrons released by the fission process convert uranium-238 nuclei into plutonium-239.
Both plutonium-239 and plutonium-241 are fissile, meaning that they can sustain a nuclear chain reaction, leading to applications in nuclear weapons and nuclear reactors. Plutonium-240 exhibits a high rate of spontaneous fission, raising the neutron flux of any sample containing it. The presence of plutonium-240 limits a plutonium sample's usability for weapons or its quality as reactor fuel, and the percentage of plutonium-240 determines its grade (weapons-grade, fuel-grade, or reactor-grade). Plutonium-238 has a half-life of 87.7 years and emits alpha particles. It is a heat source in radioisotope thermoelectric generators, which are used to power some spacecraft. Plutonium isotopes are expensive and inconvenient to separate, so particular isotopes are usually manufactured in specialized reactors.
Producing plutonium in useful quantities for the first time was a major part of the Manhattan Project during World War II that developed the first atomic bombs. The Fat Man bombs used in the Trinity nuclear test in July 1945, and in the bombing of Nagasaki in August 1945, had plutonium cores. Human radiation experiments studying plutonium were conducted without informed consent, and several criticality accidents, some lethal, occurred after the war. Disposal of plutonium waste from nuclear power plants and dismantled nuclear weapons built during the Cold War is a nuclear-proliferation and environmental concern. Other sources of plutonium in the environment are fallout from numerous above-ground nuclear tests, now banned.
'''

Am_info='''Americium is a synthetic radioactive chemical element with the symbol Am and atomic number 95. It is a transuranic member of the actinide series, in the periodic table located under the lanthanide element europium, and thus by analogy was named after the Americas. Americium was first produced in 1944 by the group of Glenn T. Seaborg from Berkeley, California, at the Metallurgical Laboratory of the University of Chicago, a part of the Manhattan Project. Although it is the third element in the transuranic series, it was discovered fourth, after the heavier curium. The discovery was kept secret and only released to the public in November 1945. Most americium is produced by uranium or plutonium being bombarded with neutrons in nuclear reactors – one tonne of spent nuclear fuel contains about 100 grams of americium. It is widely used in commercial ionization chamber smoke detectors, as well as in neutron sources and industrial gauges. Several unusual applications, such as nuclear batteries or fuel for space ships with nuclear propulsion, have been proposed for the isotope 242mAm, but they are as yet hindered by the scarcity and high price of this nuclear isomer.
Americium is a relatively soft radioactive metal with silvery appearance. Its common isotopes are 241Am and 243Am. In chemical compounds, americium usually assumes the oxidation state +3, especially in solutions. Several other oxidation states are known, ranging from +2 to +7, and can be identified by their characteristic optical absorption spectra. The crystal lattice of solid americium and its compounds contain small intrinsic radiogenic defects, due to metamictization induced by self-irradiation with alpha particles, which accumulates with time; this can cause a drift of some material properties over time, more noticeable in older samples.

'''
Cm_info='''Curium is a transuranic radioactive chemical element with the symbol Cm and atomic number 96. This element of the actinide series was named after Marie and Pierre Curie – both were known for their research on radioactivity. Curium was first intentionally produced and identified in July 1944 by the group of Glenn T. Seaborg at the University of California, Berkeley. The discovery was kept secret and only released to the public in November 1947. Most curium is produced by bombarding uranium or plutonium with neutrons in nuclear reactors – one tonne of spent nuclear fuel contains about 20 grams of curium.
Curium is a hard, dense, silvery metal with a relatively high melting point and boiling point for an actinide. Whereas it is paramagnetic at ambient conditions, it becomes antiferromagnetic upon cooling, and other magnetic transitions are also observed for many curium compounds. In compounds, curium usually exhibits valence +3 and sometimes +4, and the +3 valence is predominant in solutions. Curium readily oxidizes, and its oxides are a dominant form of this element. It forms strongly fluorescent complexes with various organic compounds, but there is no evidence of its incorporation into bacteria and archaea. When introduced into the human body, curium accumulates in the bones, lungs and liver, where it promotes cancer.
All known isotopes of curium are radioactive and have a small critical mass for a sustained nuclear chain reaction. They predominantly emit α-particles, and the heat released in this process can serve as a heat source in radioisotope thermoelectric generators, but this application is hindered by the scarcity and high cost of curium isotopes. Curium is used in production of heavier actinides and of the 238Pu radionuclide for power sources in artificial pacemakers. It served as the α-source in the alpha particle X-ray spectrometers installed on several space probes, including the Sojourner, Spirit, Opportunity and Curiosity Mars rovers and the Philae lander on comet 67P/Churyumov–Gerasimenko, to analyze the composition and structure of the surface.
'''
Bk_info='''Berkelium is a transuranic radioactive chemical element with the symbol Bk and atomic number 97. It is a member of the actinide and transuranium element series. It is named after the city of Berkeley, California, the location of the Lawrence Berkeley National Laboratory (then the University of California Radiation Laboratory) where it was discovered in December 1949. Berkelium was the fifth transuranium element discovered after neptunium, plutonium, curium and americium.
The major isotope of berkelium, 249Bk, is synthesized in minute quantities in dedicated high-flux nuclear reactors, mainly at the Oak Ridge National Laboratory in Tennessee, USA, and at the Research Institute of Atomic Reactors in Dimitrovgrad, Russia. The production of the second-most important isotope 247Bk involves the irradiation of the rare isotope 244Cm with high-energy alpha particles.
Just over one gram of berkelium has been produced in the United States since 1967. There is no practical application of berkelium outside scientific research which is mostly directed at the synthesis of heavier transuranic elements and transactinides. A 22 milligram batch of berkelium-249 was prepared during a 250-day irradiation period and then purified for a further 90 days at Oak Ridge in 2009. This sample was used to synthesize the new element tennessine for the first time in 2009 at the Joint Institute for Nuclear Research, Russia, after it was bombarded with calcium-48 ions for 150 days. This was the culmination of the Russia–US collaboration on the synthesis of the heaviest elements on the periodic table.
Berkelium is a soft, silvery-white, radioactive metal. The berkelium-249 isotope emits low-energy electrons and thus is relatively safe to handle. It decays with a half-life of 330 days to californium-249, which is a strong emitter of ionizing alpha particles. This gradual transformation is an important consideration when studying the properties of elemental berkelium and its chemical compounds, since the formation of californium brings not only chemical contamination, but also free-radical effects and self-heating from the emitted alpha particles.
'''

Cf_info='''Californium is a radioactive chemical element with the symbol Cf and atomic number 98. The element was first synthesized in 1950 at the Lawrence Berkeley National Laboratory (then the University of California Radiation Laboratory), by bombarding curium with alpha particles (helium-4 ions). It is an actinide element, the sixth transuranium element to be synthesized, and has the second-highest atomic mass of all the elements that have been produced in amounts large enough to see with the unaided eye (after einsteinium). The element was named after the university and the state of California.
Two crystalline forms exist for californium under normal pressure: one above and one below 900 °C (1,650 °F). A third form exists at high pressure. Californium slowly tarnishes in air at room temperature. Compounds of californium are dominated by the +3 oxidation state. The most stable of californium's twenty known isotopes is californium-251, which has a half-life of 898 years. This short half-life means the element is not found in significant quantities in the Earth's crust. Californium-252, with a half-life of about 2.645 years, is the most common isotope used and is produced at the Oak Ridge National Laboratory in the United States and the Research Institute of Atomic Reactors in Russia.
Californium is one of the few transuranium elements that have practical applications. Most of these applications exploit the property of certain isotopes of californium to emit neutrons. For example, californium can be used to help start up nuclear reactors, and it is employed as a source of neutrons when studying materials using neutron diffraction and neutron spectroscopy. Californium can also be used in nuclear synthesis of higher mass elements; oganesson (element 118) was synthesized by bombarding californium-249 atoms with calcium-48 ions. Users of californium must take into account radiological concerns and the element's ability to disrupt the formation of red blood cells by bioaccumulating in skeletal tissue.
'''

Es_info='''Einsteinium is a synthetic element with the symbol Es and atomic number 99. As a member of the actinide series, it is the seventh transuranic element.
Einsteinium was discovered as a component of the debris of the first hydrogen bomb explosion in 1952, and named after Albert Einstein. Its most common isotope einsteinium-253 (half-life 20.47 days) is produced artificially from decay of californium-253 in a few dedicated high-power nuclear reactors with a total yield on the order of one milligram per year. The reactor synthesis is followed by a complex process of separating einsteinium-253 from other actinides and products of their decay. Other isotopes are synthesized in various laboratories, but in much smaller amounts, by bombarding heavy actinide elements with light ions. Owing to the small amounts of produced einsteinium and the short half-life of its most easily produced isotope, there are currently almost no practical applications for it outside basic scientific research. In particular, einsteinium was used to synthesize, for the first time, 17 atoms of the new element mendelevium in 1955.
Einsteinium is a soft, silvery, paramagnetic metal. Its chemistry is typical of the late actinides, with a preponderance of the +3 oxidation state; the +2 oxidation state is also accessible, especially in solids. The high radioactivity of einsteinium-253 produces a visible glow and rapidly damages its crystalline metal lattice, with released heat of about 1000 watts per gram. Difficulty in studying its properties is due to einsteinium-253's decay to berkelium-249 and then californium-249 at a rate of about 3% per day. The isotope of einsteinium with the longest half-life, einsteinium-252 (half-life 471.7 days) would be more suitable for investigation of physical properties, but it has proven far more difficult to produce and is available only in minute quantities, and not in bulk. Einsteinium is the element with the highest atomic number which has been observed in macroscopic quantities in its pure form, and this was the common short-lived isotope einsteinium-253.Like all synthetic transuranic elements, isotopes of einsteinium are very radioactive and are considered highly dangerous to health on ingestion.
'''

Fm_info='''Fermium is a synthetic element with the symbol Fm and atomic number 100. It is an actinide and the heaviest element that can be formed by neutron bombardment of lighter elements, and hence the last element that can be prepared in macroscopic quantities, although pure fermium metal has not yet been prepared. A total of 19 isotopes are known, with 257Fm being the longest-lived with a half-life of 100.5 days.
It was discovered in the debris of the first hydrogen bomb explosion in 1952, and named after Enrico Fermi, one of the pioneers of nuclear physics. Its chemistry is typical for the late actinides, with a preponderance of the +3 oxidation state but also an accessible +2 oxidation state. Owing to the small amounts of produced fermium and all of its isotopes having relatively short half-lives, there are currently no uses for it outside basic scientific research.
'''

Md_info='''Mendelevium is a synthetic element with the symbol Md (formerly Mv) and atomic number 101. A metallic radioactive transuranic element in the actinide series, it is the first element by atomic number that currently cannot be produced in macroscopic quantities through neutron bombardment of lighter elements. It is the third-to-last actinide and the ninth transuranic element. It can only be produced in particle accelerators by bombarding lighter elements with charged particles. A total of sixteen mendelevium isotopes are known, the most stable being 258Md with a half-life of 51 days; nevertheless, the shorter-lived 256Md (half-life 1.17 hours) is most commonly used in chemistry because it can be produced on a larger scale.
Mendelevium was discovered by bombarding einsteinium with alpha particles in 1955, the same method still used to produce it today. It was named after Dmitri Mendeleev, father of the periodic table of the chemical elements. Using available microgram quantities of the isotope einsteinium-253, over a million mendelevium atoms may be produced each hour. The chemistry of mendelevium is typical for the late actinides, with a preponderance of the +3 oxidation state but also an accessible +2 oxidation state. All of the isotopes of mendelevium have relatively short half-lives, there are currently no uses for it outside basic scientific research, and  only small amounts are produced.
'''
No_info='''Nobelium is a synthetic chemical element with the symbol No and atomic number 102. It is named in honor of Alfred Nobel, the inventor of dynamite and benefactor of science. A radioactive metal, it is the tenth transuranic element and is the penultimate member of the actinide series. Like all elements with atomic number over 100, nobelium can only be produced in particle accelerators by bombarding lighter elements with charged particles. A total of twelve nobelium isotopes are known to exist; the most stable is 259No with a half-life of 58 minutes, but the shorter-lived 255No (half-life 3.1 minutes) is most commonly used in chemistry because it can be produced on a larger scale.
Chemistry experiments have confirmed that nobelium behaves as a heavier homolog to ytterbium in the periodic table. The chemical properties of nobelium are not completely known: they are mostly only known in aqueous solution. Before nobelium's discovery, it was predicted that it would show a stable +2 oxidation state as well as the +3 state characteristic of the other actinides: these predictions were later confirmed, as the +2 state is much more stable than the +3 state in aqueous solution and it is difficult to keep nobelium in the +3 state.
In the 1950s and 1960s, many claims of the discovery of nobelium were made from laboratories in Sweden, the Soviet Union, and the United States. Although the Swedish scientists soon retracted their claims, the priority of the discovery and therefore the naming of the element was disputed between Soviet and American scientists, and it was not until 1997 that International Union of Pure and Applied Chemistry (IUPAC) credited the Soviet team with the discovery, but retained nobelium, the Swedish proposal, as the name of the element due to its long-standing use in the literature.
'''

Lr_info='''Lawrencium is a synthetic chemical element with the symbol Lr (formerly Lw) and atomic number 103. It is named in honor of Ernest Lawrence, inventor of the cyclotron, a device that was used to discover many artificial radioactive elements. A radioactive metal, lawrencium is the eleventh transuranic element and is also the final member of the actinide series. Like all elements with atomic number over 100, lawrencium can only be produced in particle accelerators by bombarding lighter elements with charged particles. Thirteen isotopes of lawrencium are currently known; the most stable is 266Lr with a half-life of 11 hours, but the shorter-lived 260Lr (half-life 2.7 minutes) is most commonly used in chemistry because it can be produced on a larger scale.
Chemistry experiments have confirmed that lawrencium behaves as a heavier homolog to lutetium in the periodic table, and is a trivalent element. It thus could also be classified as the first of the 7th-period transition metals: however, its electron configuration is anomalous for its position in the periodic table, having an s2p configuration instead of the s2d configuration of its homolog lutetium. This means that lawrencium may be more volatile than expected for its position in the periodic table and have a volatility comparable to that of lead.
In the 1950s, 1960s, and 1970s, many claims of the synthesis of lawrencium of varying quality were made from laboratories in the Soviet Union and the United States. The priority of the discovery and therefore the naming of the element was disputed between Soviet and American scientists, and while the International Union of Pure and Applied Chemistry (IUPAC) initially established lawrencium as the official name for the element and gave the American team credit for the discovery, this was reevaluated in 1997, giving both teams shared credit for the discovery but not changing the element's name.
'''

Rf_info='''Rutherfordium is a synthetic chemical element with the symbol Rf and atomic number 104, named after New Zealand physicist Ernest Rutherford. As a synthetic element, it is not found in nature and can only be created in a laboratory. It is radioactive; the most stable known isotope, 267Rf, has a half-life of approximately 1.3 hours.
In the periodic table of the elements, it is a d-block element and the second of the fourth-row transition elements. It is a member of the 7th period and belongs to the group 4 elements. Chemistry experiments have confirmed that rutherfordium behaves as the heavier homologue to hafnium in group 4. The chemical properties of rutherfordium are characterized only partly. They compare well with the chemistry of the other group 4 elements, even though some calculations had indicated that the element might show significantly different properties due to relativistic effects.
In the 1960s, small amounts of rutherfordium were produced in the Joint Institute for Nuclear Research in the Soviet Union and at Lawrence Berkeley National Laboratory in California. The priority of the discovery and therefore the naming of the element was disputed between Soviet and American scientists, and it was not until 1997 that International Union of Pure and Applied Chemistry (IUPAC) established rutherfordium as the official name for the element.
'''
Db_info='''Dubnium is a synthetic chemical element with the symbol Db and atomic number 105. Dubnium is highly radioactive: the most stable known isotope, dubnium-268, has a half-life of about 28 hours. This greatly limits the extent of research on dubnium.
Dubnium does not occur naturally on Earth and is produced artificially. The Soviet Joint Institute for Nuclear Research (JINR) claimed the first discovery of the element in 1968, followed by the American Lawrence Berkeley Laboratory in 1970. Both teams proposed their names for the new element and used them without formal approval. The long-standing dispute was resolved in 1993 by an official investigation of the discovery claims by the Transfermium Working Group, formed by the International Union of Pure and Applied Chemistry and the International Union of Pure and Applied Physics, resulting in credit for the discovery being officially shared between both teams. The element was formally named dubnium in 1997 after the town of Dubna, the site of the JINR.
Theoretical research establishes dubnium as a member of group 5 in the 6d series of transition metals, placing it under vanadium, niobium, and tantalum. Dubnium should share most properties, such as its valence electron configuration and having a dominant +5 oxidation state, with the other group 5 elements, with a few anomalies due to relativistic effects. A limited investigation of dubnium chemistry has confirmed this. Solution chemistry experiments have revealed that dubnium often behaves more like niobium rather than tantalum, breaking periodic trends.
'''

Sg_info='''Seaborgium is a synthetic chemical element with the symbol Sg and atomic number 106. It is named after the American nuclear chemist Glenn T. Seaborg. As a synthetic element, it can be created in a laboratory but is not found in nature. It is also radioactive; the most stable known isotope, 269Sg, has a half-life of approximately 14 minutes.In the periodic table of the elements, it is a d-block transactinide element. It is a member of the 7th period and belongs to the group 6 elements as the fourth member of the 6d series of transition metals. Chemistry experiments have confirmed that seaborgium behaves as the heavier homologue to tungsten in group 6. The chemical properties of seaborgium are characterized only partly, but they compare well with the chemistry of the other group 6 elements.
In 1974, a few atoms of seaborgium were produced in laboratories in the Soviet Union and in the United States. The priority of the discovery and therefore the naming of the element was disputed between Soviet and American scientists, and it was not until 1997 that International Union of Pure and Applied Chemistry (IUPAC) established seaborgium as the official name for the element. It is one of only two elements named after a living person at the time of naming, the other being oganesson, element 118.
'''

Bh_info='''Bohrium is a synthetic chemical element with the symbol Bh and atomic number 107. It is named after Danish physicist Niels Bohr. As a synthetic element, it can be created in a laboratory but is not found in nature. All known isotopes of bohrium are extremely radioactive; the most stable known isotope is 270Bh with a half-life of approximately 61 seconds, though the unconfirmed 278Bh may have a longer half-life of about 690 seconds.
In the periodic table, it is a d-block transactinide element. It is a member of the 7th period and belongs to the group 7 elements as the fifth member of the 6d series of transition metals. Chemistry experiments have confirmed that bohrium behaves as the heavier homologue to rhenium in group 7. The chemical properties of bohrium are characterized only partly, but they compare well with the chemistry of the other group 7 elements.
'''
Hs_info='''Hassium is a chemical element with the symbol Hs and the atomic number 108. Hassium is highly radioactive; the most stable known isotope, 269Hs, has a half-life of approximately 16 seconds. One of its isotopes, 270Hs, has magic numbers of both protons and neutrons for deformed nuclei, which gives it greater stability against spontaneous fission. Hassium has been made only in laboratories in minuscule quantities; its possible occurrence in nature has been hypothesized but no natural hassium has been found so far.
The first attempts to synthesize element 108 were made in two different experiments at the Joint Institute for Nuclear Research (JINR) in Dubna, Moscow Oblast, Russian SFSR, Soviet Union, in 1978. More attempts were made at the same venue in 1983 and then in 1984; the latter resulted in a claim that element 108 had been produced. Later in 1984, an attempt was made at the Gesellschaft für Schwerionenforschung (GSI) in Darmstadt, Hesse, West Germany, which claimed to have synthesized it. The 1993 report by the Transfermium Working Group, formed by the International Union of Pure and Applied Chemistry and the International Union of Pure and Applied Physics, concluded the report from Darmstadt was more conclusive on its own and the major credit was assigned to the German scientists, who then chose the name hassium after the German state of Hesse.
In the periodic table of elements, hassium is a transactinide element, a member of the 7th period and group 8; it is thus the sixth member of the 6d series of transition metals. Chemistry experiments have confirmed that hassium behaves as the heavier homologue to osmium, in group 8, reacting readily with oxygen to form a volatile tetroxide. The chemical properties of hassium have only been partly characterized but they compare well with the chemistry of the other group 8 elements.
'''

Mt_info='''Meitnerium is a synthetic chemical element with the symbol Mt and atomic number 109. It is an extremely radioactive synthetic element (an element not found in nature, but can be created in a laboratory). The most stable known isotope, meitnerium-278, has a half-life of 4.5 seconds, although the unconfirmed meitnerium-282 may have a longer half-life of 67 seconds. The GSI Helmholtz Centre for Heavy Ion Research near Darmstadt, Germany, first created this element in 1982. It is named after Lise Meitner.
In the periodic table, meitnerium is a d-block transactinide element. It is a member of the 7th period and is placed in the group 9 elements, although no chemical experiments have yet been carried out to confirm that it behaves as the heavier homologue to iridium in group 9 as the seventh member of the 6d series of transition metals. Meitnerium is calculated to have similar properties to its lighter homologues, cobalt, rhodium, and iridium.
'''

Ds_info='''Darmstadtium is a chemical element with the symbol Ds and atomic number 110. It is an extremely radioactive synthetic element. The most stable known isotope, darmstadtium-281, has a half-life of approximately 12.7 seconds. Darmstadtium was first created in 1994 by the GSI Helmholtz Centre for Heavy Ion Research near the city of Darmstadt, Germany, after which it was named.
In the periodic table, it is a d-block transactinide element. It is a member of the 7th period and is placed in the group 10 elements, although no chemical experiments have yet been carried out to confirm that it behaves as the heavier homologue to platinum in group 10 as the eighth member of the 6d series of transition metals. Darmstadtium is calculated to have similar properties to its lighter homologues, nickel, palladium, and platinum.
'''

Rg_info='''Roentgenium is a chemical element with the symbol Rg and atomic number 111. It is an extremely radioactive synthetic element that can be created in a laboratory but is not found in nature. The most stable known isotope, roentgenium-282, has a half-life of 100 seconds, although the unconfirmed roentgenium-286 may have a longer half-life of about 10.7 minutes. Roentgenium was first created in 1994 by the GSI Helmholtz Centre for Heavy Ion Research near Darmstadt, Germany. It is named after the physicist Wilhelm Röntgen (also spelled Roentgen), who discovered X-rays.In the periodic table, it is a d-block transactinide element. It is a member of the 7th period and is placed in the group 11 elements, although no chemical experiments have been carried out to confirm that it behaves as the heavier homologue to gold in group 11 as the ninth member of the 6d series of transition metals. Roentgenium is calculated to have similar properties to its lighter homologues, copper, silver, and gold, although it may show some differences from them.'''

Cn_info='''Copernicium is a synthetic chemical element with the symbol Cn and atomic number 112. Its known isotopes are extremely radioactive, and have only been created in a laboratory. The most stable known isotope, copernicium-285, has a half-life of approximately 28 seconds. Copernicium was first created in 1996 by the GSI Helmholtz Centre for Heavy Ion Research near Darmstadt, Germany. It is named after the astronomer Nicolaus Copernicus.
In the periodic table of the elements, copernicium is a d-block transactinide element and a group 12 element. During reactions with gold, it has been shown to be an extremely volatile substance, so much so that it is possibly a gas or a volatile liquid at standard temperature and pressure.
Copernicium is calculated to have several properties that differ from its lighter homologues in group 12, zinc, cadmium and mercury; due to relativistic effects, it may give up its 6d electrons instead of its 7s ones, and it may have more similarities to the noble gases such as radon rather than its group 12 homologues. Copernicium has also been calculated to possibly show the oxidation state +4, while mercury shows it in only one compound of disputed existence and zinc and cadmium do not show it at all. It has also been predicted to be more difficult to oxidize copernicium from its neutral state than the other group 12 elements, and indeed copernicium is expected to be the most noble metal on the periodic table. Solid copernicium is expected to be bound mostly by dispersion forces, like the noble gases; predictions on its band structure are varied, ranging from a noble metal to a semiconductor or even an insulator.
'''

Nh_info='''Nihonium is a synthetic chemical element with the symbol Nh and atomic number 113. It is extremely radioactive; its most stable known isotope, nihonium-286, has a half-life of about 10 seconds. In the periodic table, nihonium is a transactinide element in the p-block. It is a member of period 7 and group 13 (boron group).
Nihonium was first reported to have been created in 2003 by a Russian–American collaboration at the Joint Institute for Nuclear Research (JINR) in Dubna, Russia, and in 2004 by a team of Japanese scientists at Riken in Wakō, Japan. The confirmation of their claims in the ensuing years involved independent teams of scientists working in the United States, Germany, Sweden, and China, as well as the original claimants in Russia and Japan. In 2015, the IUPAC/IUPAP Joint Working Party recognised the element and assigned the priority of the discovery and naming rights for the element to Riken, as it judged that they had demonstrated that they had observed element 113 before the JINR team did so. The Riken team suggested the name nihonium in 2016, which was approved in the same year. The name comes from the common Japanese name for Japan (日本, nihon).
Very little is known about nihonium, as it has only been made in very small amounts that decay away within seconds. The anomalously long lives of some superheavy nuclides, including some nihonium isotopes, are explained by the "island of stability" theory. Experiments support the theory, with the half-lives of the confirmed nihonium isotopes increasing from milliseconds to seconds as neutrons are added and the island is approached. Nihonium has been calculated to have similar properties to its homologues boron, aluminium, gallium, indium, and thallium. All but boron are post-transition metals, and nihonium is expected to be a post-transition metal as well. It should also show several major differences from them; for example, nihonium should be more stable in the +1 oxidation state than the +3 state, like thallium, but in the +1 state nihonium should behave more like silver and astatine than thallium. Preliminary experiments in 2017 showed that elemental nihonium is not very volatile; its chemistry remains largely unexplored.
'''

Fl_info='''Flerovium is a superheavy artificial chemical element with the symbol Fl and atomic number 114. It is an extremely radioactive synthetic element. The element is named after the Flerov Laboratory of Nuclear Reactions of the Joint Institute for Nuclear Research in Dubna, Russia, where the element was discovered in 1998. The name of the laboratory, in turn, honours the Russian physicist Georgy Flyorov (Флёров in Cyrillic, hence the transliteration of "yo" to "e"). The name was adopted by IUPAC on 30 May 2012.
In the periodic table of the elements, it is a transactinide element in the p-block. It is a member of the 7th period and is the heaviest known member of the carbon group; it is also the heaviest element whose chemistry has been investigated. Initial chemical studies performed in 2007–2008 indicated that flerovium was unexpectedly volatile for a group 14 element; in preliminary results it even seemed to exhibit properties similar to those of the noble gases. More recent results show that flerovium's reaction with gold is similar to that of copernicium, showing that it is a very volatile element that may even be gaseous at standard temperature and pressure, that it would show metallic properties, consistent with it being the heavier homologue of lead, and that it would be the least reactive metal in group 14. The question of whether flerovium behaves more like a metal or a noble gas is still unresolved as of 2018.
About 90 atoms of flerovium have been observed: 58 were synthesized directly, and the rest were made from the radioactive decay of heavier elements. All of these flerovium atoms have been shown to have mass numbers from 284 to 290. The most stable known flerovium isotope, flerovium-289, has a half-life of around 1.9 seconds, but it is possible that the unconfirmed flerovium-290 with one extra neutron may have a longer half-life of 19 seconds; this would be one of the longest half-lives of any isotope of any element at these farthest reaches of the periodic table. Flerovium is predicted to be near the centre of the theorized island of stability, and it is expected that heavier flerovium isotopes, especially the possibly doubly magic flerovium-298, may have even longer half-lives.
'''

Mc_info='''Moscovium is a synthetic chemical element with the symbol Mc and atomic number 115. It was first synthesized in 2003 by a joint team of Russian and American scientists at the Joint Institute for Nuclear Research (JINR) in Dubna, Russia. In December 2015, it was recognized as one of four new elements by the Joint Working Party of international scientific bodies IUPAC and IUPAP. On 28 November 2016, it was officially named after the Moscow Oblast, in which the JINR is situated.Moscovium is an extremely radioactive element: its most stable known isotope, moscovium-290, has a half-life of only 0.65 seconds. In the periodic table, it is a p-block transactinide element. It is a member of the 7th period and is placed in group 15 as the heaviest pnictogen, although it has not been confirmed to behave as a heavier homologue of the pnictogen bismuth. Moscovium is calculated to have some properties similar to its lighter homologues, nitrogen, phosphorus, arsenic, antimony, and bismuth, and to be a post-transition metal, although it should also show several major differences from them. In particular, moscovium should also have significant similarities to thallium, as both have one rather loosely bound electron outside a quasi-closed shell. About 100 atoms of moscovium have been observed to date, all of which have been shown to have mass numbers from 287 to 290.
'''

Lv_info='''Livermorium is a synthetic chemical element with the symbol Lv and has an atomic number of 116. It is an extremely radioactive element that has only been created in the laboratory and has not been observed in nature. The element is named after the Lawrence Livermore National Laboratory in the United States, which collaborated with the Joint Institute for Nuclear Research (JINR) in Dubna, Russia to discover livermorium during experiments made between 2000 and 2006. The name of the laboratory refers to the city of Livermore, California where it is located, which in turn was named after the rancher and landowner Robert Livermore. The name was adopted by IUPAC on May 30, 2012. Four isotopes of livermorium are known, with mass numbers between 290 and 293 inclusive; the longest-lived among them is livermorium-293 with a half-life of about 60 milliseconds. A fifth possible isotope with mass number 294 has been reported but not yet confirmed.
In the periodic table, it is a p-block transactinide element. It is a member of the 7th period and is placed in group 16 as the heaviest chalcogen, although it has not been confirmed to behave as the heavier homologue to the chalcogen polonium. Livermorium is calculated to have some similar properties to its lighter homologues (oxygen, sulfur, selenium, tellurium, and polonium), and be a post-transition metal, although it should also show several major differences from them.
'''

Ts_info='''Tennessine is a synthetic chemical element with the symbol Ts and atomic number 117. It is the second-heaviest known element and the penultimate element of the 7th period of the periodic table.
The discovery of tennessine was officially announced in Dubna, Russia, by a Russian–American collaboration in April 2010, which makes it the most recently discovered element as of 2020. One of its daughter isotopes was created directly in 2011, partially confirming the results of the experiment. The experiment itself was repeated successfully by the same collaboration in 2012 and by a joint German–American team in May 2014. In December 2015, the Joint Working Party of the International Union of Pure and Applied Chemistry (IUPAC) and the International Union of Pure and Applied Physics, which evaluates claims of discovery of new elements, recognized the element and assigned the priority to the Russian–American team. In June 2016, the IUPAC published a declaration stating that the discoverers had suggested the name tennessine after Tennessee, United States. In November 2016, they officially adopted the name "tennessine".
Tennessine may be located in the "island of stability", a concept that explains why some superheavy elements are more stable compared to an overall trend of decreasing stability for elements beyond bismuth on the periodic table. The synthesized tennessine atoms have lasted tens and hundreds of milliseconds. In the periodic table, tennessine is expected to be a member of group 17, all other members of which are halogens. Some of its properties may significantly differ from those of the halogens due to relativistic effects. As a result, tennessine is expected to be a volatile metal that neither forms anions nor achieves high oxidation states. A few key properties, such as its melting and boiling points and its first ionization energy, are nevertheless expected to follow the periodic trends of the halogens.'''

Og_info='''Oganesson is a synthetic chemical element with the symbol Og and atomic number 118. It was first synthesized in
2002 at the Joint Institute for Nuclear Research (JINR) in Dubna, near Moscow, Russia, by a joint team of Russian and
American scientists. In December 2015, it was recognized as one of four new elements by the Joint Working Party of the
international scientific bodies IUPAC and IUPAP. It was formally named on 28 November 2016. The name is in line with the
tradition of honoring a scientist, in this case the nuclear physicist Yuri Oganessian, who has played a leading role in the
discovery of the heaviest elements in the periodic table. It is one of only two elements named after a person who was alive at the time of naming, the other being seaborgium, and the only element whose namesake is alive today.Oganesson has the highest atomic number and highest atomic mass of all known elements. The radioactive oganesson atom is very unstable, and since 2005, only five (possibly six) atoms of the isotope 294Og have been detected. Although this allowed very little experimental characterization of its properties and possible compounds, theoretical calculations have resulted in many predictions, including some surprising ones. For example, although oganesson is a member of group 18 (the noble gases) – the first synthetic element to be so – it may be significantly reactive, unlike all the other elements of that group. It was formerly thought to be a gas under normal conditions but is now predicted to be a solid due to relativistic effects. On the periodic table of the elements it is a p-block element and the last one of period 7.
'''









# this section contains all the main functions for all the buttons

# here are the fuctions to display after button click




def H_page():    
    pt.destroy()
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Hydrogen(H):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1766)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=1 , Group=1 ,Period=1 ,Block= S, CAS Number=1333-74-0')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'1.00794' , "Oxidation_state = ":'[-1,+1]' , "Atomic_radius (pm)= ":'53',
                       "Covelent_radius(pm) = ":'31 (0.16%  error)' ,"Van der waals radius (pm)=":'120', "Boiling_point(Celcius) = " :'-252.87',
                       "Melting_point(Celcius) =":'-259.14',
                       "Electron_affinity( kJ / mol) = ":'72.8',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',"Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452', "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',"Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.332'
                      }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,H_info)

    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
    

  
def He_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Heilum(He):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1895)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=2 , Group=18 ,Period=1 ,Block= S , CAS Number=7440-59-7')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'4.002602' ,
                       "Oxidation_state = ":'[0]' ,
                       "Atomic_radius (pm)= ":'31',
                       "Covelent_radius(pm) = ":'28 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'140',
                       "Boiling_point(Celcius) = " :'-268.93',
                       "Melting_point(Celcius) =":'---',
                       "Electron_affinity( kJ / mol) = ":'0',
                       "Refractive_index = ": '1.000035',
                       "Speed_of_sound( m/s) = ": '970',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'5193.1',
                       "Thermal conductivity (W/m K)=":'0.1513',
                       "Electronegetivity=":'0',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,He_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
    
  
def Li_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium(Li):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'167',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kJ / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'520.2',
                       "Speed_of_sound( m/s) = ": '6000',
                       "Latent heat of Fusion (KJ/mol)=":'3',
                       "Latent heat of Vapourization (kJ/mol)=":'147',
                       "Mohs hardness=":'0.6',
                       "Shear modulus (GPa)= ":'4.2',
                       "Young's modulus (GPa)=":'4.9',
                       "Specific heat (J/kgK)=":'3570',
                       "Thermal conductivity (W/m K)=":'85',
                       "Electrical conductivity (S/m)=":'1.1x10^7',
                       "volume magnetic suceptibility =":'1.37x10^-5',
                       "Mass magnetic suceptibility =":'2.56x10^-8',
                       "Molar magnetic suceptibility =":'1.78x10^-10',
                       "Resistivity (ohm*m)=":'9.4x10^-8',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Li_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Be_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Beryllium(Be):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1797)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=4 , Group=2 ,Period=2 ,Block= S , CAS Number=7440-41-7')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'9.0121831' ,
                       "Oxidation_state = ":'[+2]' ,
                       "Atomic_radius (pm)= ":'112',
                       "Covelent_radius(pm) = ":'96' ,
                       "Boiling_point(Celcius) = " :'2470',
                       "Melting_point(Celcius) =":'1287',
                       "Electron_affinity( kJ / mol) = ":'0',
                       "First ionization energy (kJ/mol)=":'899.5',
                       "Speed_of_sound( m/s) = ": '13000',
                       "Latent heat of Fusion (KJ/mol)=":'7.95',
                       "Latent heat of Vapourization (kJ/mol)=":'297',
                       "Specific heat (J/kgK)=":'1820',
                       "Thermal conductivity (W/m K)=":'190',
                       "Electronegetivity=":'1.57',
                       "Neutron cross-section (barn)=":'0.0092'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Be_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def B_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Boron(B):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1808)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=5 , Group=13 ,Period=2 ,Block= p , CAS Number=7440-42-8')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'10.81' ,
                       "Oxidation_state = ":'[+3]' ,
                       "Atomic_radius (pm)= ":'87',
                       "Covelent_radius(pm) = ":'84' ,
                       "Boiling_point(Celcius) = " :'4000',
                       "Melting_point(Celcius) =":'2075',
                       "Electron_affinity( kJ / mol) = ":'26.7',
                       "First ionization energy (kJ/mol)=":'800.6',
                       "Speed_of_sound( m/s) = ": '16200',
                       "Latent heat of Fusion (KJ/mol)=":'50',
                       "Latent heat of Vapourization (kJ/mol)=":'507',
                       "Specific heat (J/kgK)=":'1030',
                       "Thermal conductivity (W/m K)=":'27',
                       "Electronegetivity=":'2.04',
                       "Neutron cross-section (barn)=":'755'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,B_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def C_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Carbon(C):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : Prehistoric)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=6 , Group=14 ,Period=2 ,Block= p , CAS Number=7440-44-0')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'12.011' ,
                       "Oxidation_state = ":'[-4,+2,+4]' ,
                       "Atomic_radius (pm)= ":'67',
                       "Covelent_radius(pm) = ":'76 ' ,
                       "Van der waals radius (pm)=":'170',
                       "Boiling_point(Celcius) = " :'4027',
                       "Melting_point(Celcius) =":'3550',
                       "Electron_affinity( kJ / mol) = ":'153.9',
                       "First ionization energy (kJ/mol)=":'1086.5',
                       "Speed_of_sound( m/s) = ": '18350',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'140',
                       "Electronegetivity=":'2.55',
                       "Neutron cross-section (barn)=":'0.00035'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,C_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def N_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Nitrogen(N):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1772)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=7 , Group=15 ,Period=2 ,Block= p , CAS Number=7727-37-9')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'14.007' ,
                       "Oxidation_state = ":'[-3,-2,-1,+1,+2,+3,+4,+5]' ,
                       "Atomic_radius (pm)= ":'56',
                       "Covelent_radius(pm) = ":'71 ' ,
                       "Van der waals radius (pm)=":'155',
                       "Boiling_point(Celcius) = " :'-195.79',
                       "Melting_point(Celcius) =":'-210.1',
                       "Electron_affinity( kj / mol) = ":'7',
                       "First ionization energy (kJ/mol)=":'1402.3',
                       "Speed_of_sound( m/s) = ": '333.6',
                       "Latent heat of Fusion (KJ/mol)=":'0.36',
                       "Latent heat of Vapourization (kJ/mol)=":'2.79',
                       "Specific heat (J/kgK)=":'1040',
                       "Thermal conductivity (W/m K)=":'0.02583',
                       "Electronegetivity=":'3.04',
                       "Neutron cross-section (barn)=":'1.91'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,N_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def O_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Oxygen(O):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1774)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=8 , Group=16 ,Period=2 ,Block= p , CAS Number=7782-44-7')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'15.999' ,
                       "Oxidation_state = ":'[-2,-1,+1,+2]' ,
                       "Atomic_radius (pm)= ":'48',
                       "Covelent_radius(pm) = ":'66 ' ,
                       "Van der waals radius (pm)=":'152',
                       "Boiling_point(Celcius) = " :'-182.9',
                       "Melting_point(Celcius) =":'-218.3',
                       "Electron_affinity( kj / mol) = ":'141',
                       "First ionization energy (kJ/mol)=":'1313.9',
                       "Speed_of_sound( m/s) = ": '317.5',
                       "Latent heat of Fusion (KJ/mol)=":'0.222',
                       "Latent heat of Vapourization (kJ/mol)=":'3.41',
                       "Specific heat (J/kgK)=":'919',
                       "Thermal conductivity (W/m K)=":'0.02658',
                       "Electronegetivity=":'3.44',
                       "Neutron cross-section (barn)=":'0.00028'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,O_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def F_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Flurine(F):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1886)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=9 , Group=17 ,Period=2 ,Block= p , CAS Number=7782-41-4')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'18.998403163' ,
                       "Oxidation_state = ":'[-1]' ,
                       "Atomic_radius (pm)= ":'42',
                       "Covelent_radius(pm) = ":'57' ,
                       "Van der waals radius (pm)=":'147',
                       "Boiling_point(Celcius) = " :'-188.12',
                       "Melting_point(Celcius) =":'-219.6',
                       "Electron_affinity( kj / mol) = ":'328',
                       "First ionization energy (kJ/mol)=":'1681',
                       "Speed_of_sound( m/s) = ": '---',
                       "Latent heat of Fusion (KJ/mol)=":'0.26',
                       "Latent heat of Vapourization (kJ/mol)=":'3.27',
                       "Specific heat (J/kgK)=":'824',
                       "Thermal conductivity (W/m K)=":'0.0277',
                       "Electronegetivity=":'3.98',
                       "Neutron cross-section (barn)=":'0.0096'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,F_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ne_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Neon(Ne):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1898)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=10 , Group=18 ,Period=2 ,Block= p , CAS Number=7440-01-9')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'20.1797' ,
                       "Oxidation_state = ":'[0]' ,
                       "Atomic_radius (pm)= ":'38',
                       "Covelent_radius(pm) = ":'58' ,
                       "Van der waals radius (pm)=":'154',
                       "Boiling_point(Celcius) = " :'-246.59',
                       "Melting_point(Celcius) =":'-248.59',
                       "Electron_affinity( kj / mol) = ":'0',
                       "First ionization energy (kJ/mol)=":'2080.7',
                       "Speed_of_sound( m/s) = ": '936',
                       "Latent heat of Fusion (KJ/mol)=":'0.34',
                       "Latent heat of Vapourization (kJ/mol)=":'1.75',
                       "Specific heat (J/kgK)=":'1030',
                       "Thermal conductivity (W/m K)=":'0.0491',
                       "Electronegetivity=":'--',
                       "Neutron cross-section (barn)=":'0.04'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ne_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Na_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Sodium(Na):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1807)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=11 , Group=1 ,Period=3 ,Block= S , CAS Number=7440-23-5')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'22.9897928' ,
                       "Oxidation_state = ":'[+1]' ,
                       "Atomic_radius (pm)= ":'190',
                       "Covelent_radius(pm) = ":'166' ,
                       "Van der waals radius (pm)=":'227',
                       "Boiling_point(Celcius) = " :'883',
                       "Melting_point(Celcius) =":'97.72',
                       "Electron_affinity( kj / mol) = ":'52.8',
                       "First ionization energy (kJ/mol)=":'495.8',
                       "Speed_of_sound( m/s) = ": '3200',
                       "Latent heat of Fusion (KJ/mol)=":'2.6',
                       "Latent heat of Vapourization (kJ/mol)=":'97.7',
                       "Specific heat (J/kgK)=":'1230',
                       "Thermal conductivity (W/m K)=":'140',
                       "Electronegetivity=":'0.93',
                       "Neutron cross-section (barn)=":'0.053'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Na_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Mg_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Magnesium(Mg):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1755)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=12 , Group=2 ,Period=3 ,Block= S , CAS Number=7439-95-4')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'24.305' ,
                       "Oxidation_state = ":'[+2]' ,
                       "Atomic_radius (pm)= ":'145',
                       "Covelent_radius(pm) = ":'141' ,
                       "Van der waals radius (pm)=":'173',
                       "Boiling_point(Celcius) = " :'1090',
                       "Melting_point(Celcius) =":'650',
                       "Electron_affinity( kj / mol) = ":'0',
                       "First ionization energy (kJ/mol)=":'737.7',
                       "Speed_of_sound( m/s) = ": '4602',
                       "Latent heat of Fusion (KJ/mol)=":'8.7',
                       "Latent heat of Vapourization (kJ/mol)=":'128',
                       "Specific heat (J/kgK)=":'1020',
                       "Thermal conductivity (W/m K)=":'160',
                       "Electronegetivity=":'1.31',
                       "Neutron cross-section (barn)=":'0.063'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Mg_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Al_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Aluminium(Al):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1825)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=13 , Group=13 ,Period=3 ,Block= p , CAS Number=7429-90-5')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'26.9815385' ,
                       "Oxidation_state = ":'[+3]' ,
                       "Atomic_radius (pm)= ":'118',
                       "Covelent_radius(pm) = ":'121' ,
                       "Van der waals radius (pm)=":'---',
                       "Boiling_point(Celcius) = " :'2519',
                       "Melting_point(Celcius) =":'660.32',
                       "Electron_affinity( kj / mol) = ":'42.5',
                       "First ionization energy (kJ/mol)=":'577.5',
                       "Speed_of_sound( m/s) = ": '5100',
                       "Latent heat of Fusion (KJ/mol)=":'10.7',
                       "Latent heat of Vapourization (kJ/mol)=":'293',
                       "Specific heat (J/kgK)=":'904',
                       "Thermal conductivity (W/m K)=":'235',
                       "Electronegetivity=":'1.61',
                       "Neutron cross-section (barn)=":'0.233'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Al_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Si_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Silicon(Si):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1824)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=14 , Group=14 ,Period=3 ,Block= p , CAS Number=7440-21-3')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'28.085' ,
                       "Oxidation_state = ":'[-4,+4,+2]' ,
                       "Atomic_radius (pm)= ":'111',
                       "Covelent_radius(pm) = ":'111' ,
                       "Van der waals radius (pm)=":'210',
                       "Boiling_point(Celcius) = " :'2900',
                       "Melting_point(Celcius) =":'1414',
                       "Electron_affinity( kj / mol) = ":'133.6',
                       "First ionization energy (kJ/mol)=":'786.5',
                       "Speed_of_sound( m/s) = ": '2200',
                       "Latent heat of Fusion (KJ/mol)=":'50.2',
                       "Latent heat of Vapourization (kJ/mol)=":'359',
                       "Specific heat (J/kgK)=":'710',
                       "Thermal conductivity (W/m K)=":'150',
                       "Electronegetivity=":'1.9',
                       "Neutron cross-section (barn)=":'171'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Si_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def P_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Phosphorus(P):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1669)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=15 , Group=15 ,Period=3 ,Block= p , CAS Number=7723-14-0')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'30.973761998' ,
                       "Oxidation_state = ":'[+3,-3,+4,+5]' ,
                       "Atomic_radius (pm)= ":'98',
                       "Covelent_radius(pm) = ":'107' ,
                       "Van der waals radius (pm)=":'180',
                       "Boiling_point(Celcius) = " :'280.5',
                       "Melting_point(Celcius) =":'44.2',
                       "Electron_affinity( kj / mol) = ":'72',
                       "First ionization energy (kJ/mol)=":'1011.8',
                       "Refractive_index = ": '1.001212',
                       "Speed_of_sound( m/s) = ": '---',
                       "Latent heat of Fusion (KJ/mol)=":'0.64',
                       "Latent heat of Vapourization (kJ/mol)=":'12.4',
                       "Specific heat (J/kgK)=":'769.7',
                       "Thermal conductivity (W/m K)=":'0.236',
                       "Electronegetivity=":'2.19',
                       "Neutron cross-section (barn)=":'0.18'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,P_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

#
def S_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Sulphur(S):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 500BC)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=16 , Group=16 ,Period=3 ,Block= p , CAS Number=7704-34-9')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'32.06' ,
                       "Oxidation_state = ":'[-2,+2,+4,+6]' ,
                       "Atomic_radius (pm)= ":'88',
                       "Covelent_radius(pm) = ":'105' ,
                       "Van der waals radius (pm)=":'180',
                       "Boiling_point(Celcius) = " :'444.72',
                       "Melting_point(Celcius) =":'115.21',
                       "Electron_affinity( kj / mol) = ":'200',
                       "First ionization energy (kJ/mol)=":'999.6',
                       "Refractive_index = ": '1.001111',
                       "Speed_of_sound( m/s) = ": '_______',
                       "Latent heat of Fusion (KJ/mol)=":'1.73',
                       "Latent heat of Vapourization (kJ/mol)=":'9.8',
                       "Specific heat (J/kgK)=":'705',
                       "Thermal conductivity (W/m K)=":'0.205',
                       "Electronegetivity=":'2.58',
                       "Neutron cross-section (barn)=":'0.52'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,S_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Cl_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Chlorine(Cl):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1774)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=17 , Group=3 ,Period=17 ,Block= p , CAS Number=7782-50-5')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'35.45' ,
                       "Oxidation_state = ":'[-1,+1,+3,+5,+7]' ,
                       "Atomic_radius (pm)= ":'79',
                       "Covelent_radius(pm) = ":'102' ,
                       "Van der waals radius (pm)=":'175',
                       "Boiling_point(Celcius) = " :'-34.04',
                       "Melting_point(Celcius) =":'-101.5',
                       "Electron_affinity( kj / mol) = ":'349',
                       "First ionization energy (kJ/mol)=":'1251.2',
                       "Refractive_index = ": '1.000773',
                       "Speed_of_sound( m/s) = ": '206',
                       "Latent heat of Fusion (KJ/mol)=":'3.2',
                       "Latent heat of Vapourization (kJ/mol)=":'10.2',
                       "Specific heat (J/kgK)=":'478.2',
                       "Thermal conductivity (W/m K)=":'0.0089',
                       "Electronegetivity=":'3.16',
                       "Neutron cross-section (barn)=":'35.3'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cl_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

#from here you HAVE TO make corrections or edit(whatever you say)
def Ar_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Argon(Ar):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1894)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=18 , Group=18 ,Period=3 ,Block= P , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ar_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def K_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Potassium(K):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1807)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=19 , Group=1 ,Period=4 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'38' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,K_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ca_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Calcium(Ca):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1808)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=20 , Group=2 ,Period=4 ,Block= S , CAS Number=7440-70-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'40.078' ,
                       "Oxidation_state = ":'[+2]' ,
                       "Atomic_radius (pm)= ":'194',
                       "Covelent_radius(pm) = ":'176' ,
                       "Van der waals radius (pm)=":'----',
                       "Boiling_point(Celcius) = " :'1484',
                       "Melting_point(Celcius) =":'842',
                       "Electron_affinity( kj / mol) = ":'2.37',
                       "First ionization energy (kJ/mol)=":'589.8',
                       "Refractive_index = ": '----',
                       "Speed_of_sound( m/s) = ": '3810',
                       "Latent heat of Fusion (KJ/mol)=":'8.54',
                       "Latent heat of Vapourization (kJ/mol)=":'155',
                       "Specific heat (J/kgK)=":'631',
                       "Thermal conductivity (W/m K)=":'200',
                       "Electronegetivity=":'1',
                       "Neutron cross-section (barn)=":'0.43'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ca_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Sc_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Scandium(Sc):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1879)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=21 , Group=3 ,Period=4 ,Block= d , CAS Number=7440-20-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'44.95908' ,
                       "Oxidation_state = ":'[+3]' ,
                       "Atomic_radius (pm)= ":'184',
                       "Covelent_radius(pm) = ":'170' ,
                       "Van der waals radius (pm)=":'----',
                       "Boiling_point(Celcius) = " :'2830',
                       "Melting_point(Celcius) =":'1541',
                       "Electron_affinity( kj / mol) = ":'18.1',
                       "First ionization energy (kJ/mol)=":'633.1',
                       "Refractive_index = ": '---',
                       "Speed_of_sound( m/s) = ": '---',
                       "Latent heat of Fusion (KJ/mol)=":'16',
                       "Latent heat of Vapourization (kJ/mol)=":'318',
                       "Specific heat (J/kgK)=":'567',
                       "Thermal conductivity (W/m K)=":'16',
                       "Electronegetivity=":'1.36',
                       "Neutron cross-section (barn)=":'27.2'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sc_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ti_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Titanium(Ti):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1794)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=22 , Group=4 ,Period=4 ,Block= d , CAS Number=7440-32-6')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'47.867',
                       "Oxidation_state = ":'[+2,+3,+4]' ,
                       "Atomic_radius (pm)= ":'176',
                       "Covelent_radius(pm) = ":'160' ,
                       "Van der waals radius (pm)=":'---',
                       "Boiling_point(Celcius) = " :'3287',
                       "Melting_point(Celcius) =":'1668',
                       "Electron_affinity( kj / mol) = ":'7.6',
                       "First ionization energy (kJ/mol)=":'658.8',
                       "Refractive_index = ": '-----',
                       "Speed_of_sound( m/s) = ": '4140',
                       "Latent heat of Fusion (KJ/mol)=":'18.7',
                       "Latent heat of Vapourization (kJ/mol)=":'425',
                       "Specific heat (J/kgK)=":'520',
                       "Thermal conductivity (W/m K)=":'22',
                       "Electronegetivity=":'1.54',
                       "Neutron cross-section (barn)=":'6.1'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ti_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def V_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Vanadium(V):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1830)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=23 , Group=5 ,Period=4 ,Block= d , CAS Number=7440-62-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'50.9415' ,
                       "Oxidation_state = ":'[+1,+2,+3,+4,+5]' ,
                       "Atomic_radius (pm)= ":'134',
                       "Covelent_radius(pm) = ":'125' ,
                       "Van der waals radius (pm)=":'----',
                       "Boiling_point(Celcius) = " :'3407.0',
                       "Melting_point(Celcius) =":'1910',
                       "Electron_affinity( kj / mol) = ":'50.6',
                       "First ionization energy (kJ/mol)=":'650.9',
                       "Refractive_index = ": '----',
                       "Speed_of_sound( m/s) = ": '4560',
                       "Latent heat of Fusion (KJ/mol)=":'22.8',
                       "Latent heat of Vapourization (kJ/mol)=":'453',
                       "Specific heat (J/kgK)=":'489',
                       "Thermal conductivity (W/m K)=":'31',
                       "Electronegetivity=":'1.63',
                       "Neutron cross-section (barn)=":'5.06'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,V_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Cr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Chromium(Cr):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1797)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=24 , Group=7 ,Period=4 ,Block= d , CAS Number=7440-47-3')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'51.9961' ,
                       "Oxidation_state = ":'[-1,+1]' ,#from here
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Mn_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Manganese(Mn):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1774)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=25 , Group=7 ,Period=4 ,Block=d , CAS Number=7439-96-5')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'54.938044' ,
                       "Oxidation_state = ":'[-1,+2,+3,+4,+5,+6,+7]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'139' ,
                       "Boiling_point(Celcius) = " :'2061',
                       "Melting_point(Celcius) =":'1246',
                       "Electron_affinity( kj / mol) = ":'0',
                       "First ionization energy (kJ/mol)=":'717.3',
                       "Speed_of_sound( m/s) = ": '5150',
                       "Latent heat of Fusion (KJ/mol)=":'13.2',
                       "Latent heat of Vapourization (kJ/mol)=":'220',
                       "Specific heat (J/kgK)=":'479',
                       "Thermal conductivity (W/m K)=":'7.8',
                       "Electronegetivity=":'1.55',
                       "Neutron cross-section (barn)=":'13.3'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Mn_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
#from here
def Fe_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Iron(Fe):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 2000 BC)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=26 , Group=8 ,Period=4 ,Block= d , CAS Number=7439-89-6')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'55.845' ,
                       "Oxidation_state = ":'[-2,+2,+3]' ,
                       "Atomic_radius (pm)= ":'156',
                       "Covelent_radius(pm) = ":'132' ,
                       "Boiling_point(Celcius) = " :'2861',
                       "Melting_point(Celcius) =":'1538',
                       "Electron_affinity( kj / mol) = ":'15.7',
                       "First ionization energy (kJ/mol)=":'762.5',
                       "Speed_of_sound( m/s) = ": '4910',
                       "Latent heat of Fusion (KJ/mol)=":'13.8',
                       "Latent heat of Vapourization (kJ/mol)=":'347',
                       "Specific heat (J/kgK)=":'449',
                       "Thermal conductivity (W/m K)=":'80',
                       "Electronegetivity=":'1.83',
                       "Neutron cross-section (barn)=":'2.56'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Fe_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Co_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Cobalt(Co):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1735)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=27 , Group=9 ,Period=4 ,Block= d , CAS Number=7440-48-4')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'58.933194' ,
                       "Oxidation_state = ":'[-1,+2,+3]' ,
                       "Atomic_radius (pm)= ":'152',
                       "Covelent_radius(pm) = ":'126' ,
                       "Boiling_point(Celcius) = " :'2927',
                       "Melting_point(Celcius) =":'1495',
                       "Electron_affinity( kj / mol) = ":'63.7',
                       "First ionization energy (kJ/mol)=":'760.4',
                       "Speed_of_sound( m/s) = ": '4720',
                       "Latent heat of Fusion (KJ/mol)=":'16.2',
                       "Latent heat of Vapourization (kJ/mol)=":'375',
                       "Specific heat (J/kgK)=":'421',
                       "Thermal conductivity (W/m K)=":'100',
                       "Electronegetivity=":'1.88',
                       "Neutron cross-section (barn)=":'37.2'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Co_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ni_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Nickel(Ni):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1751)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=28 , Group=10 ,Period=4 ,Block= d , CAS Number=7440-02-0')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'58.6934' ,
                       "Oxidation_state = ":'[-1,+2,+3]' ,
                       "Atomic_radius (pm)= ":'149',
                       "Covelent_radius(pm) = ":'124' ,
                       "Van der waals radius (pm)=":'163',
                       "Boiling_point(Celcius) = " :'2913',
                       "Melting_point(Celcius) =":'1455',
                       "Electron_affinity( kj / mol) = ":'112',
                       "First ionization energy (kJ/mol)=":'737.1',
                       "Speed_of_sound( m/s) = ": '4970',
                       "Latent heat of Fusion (KJ/mol)=":'17.2',
                       "Latent heat of Vapourization (kJ/mol)=":'378',
                       "Specific heat (J/kgK)=":'445',
                       "Thermal conductivity (W/m K)=":'91',
                       "Electronegetivity=":'1.91',
                       "Neutron cross-section (barn)=":'37.2'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ni_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Cu_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Copper(Cu):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 8000 BC)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=29 , Group=11 ,Period=4 ,Block= d , CAS Number=7440-50-8')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'63.546' ,
                       "Oxidation_state = ":'[+1,+2]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'132' ,
                       "Van der waals radius (pm)=":'140',
                       "Boiling_point(Celcius) = " :'2562',
                       "Melting_point(Celcius) =":'1084.62',
                       "Electron_affinity( kj / mol) = ":'118.4',
                       "First ionization energy (kJ/mol)=":'745.5',
                       "Speed_of_sound( m/s) = ": '3570',
                       "Latent heat of Fusion (KJ/mol)=":'13.1',
                       "Latent heat of Vapourization (kJ/mol)=":'300',
                       "Specific heat (J/kgK)=":'384.4',
                       "Thermal conductivity (W/m K)=":'400',
                       "Electronegetivity=":'1.9',
                       "Neutron cross-section (barn)=":'3.78'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cu_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

#from here
def Zn_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Zinc(Zn):')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1500)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=30 , Group=12 ,Period=4 ,Block= d , CAS Number=7440-66-6')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'65.38' ,
                       "Oxidation_state = ":'[+2]' ,
                       "Atomic_radius (pm)= ":'142',
                       "Covelent_radius(pm) = ":'122' ,
                       "Van der waals radius (pm)=":'139',
                       "Boiling_point(Celcius) = " :'907',
                       "Melting_point(Celcius) =":'419',
                       "Electron_affinity( kj / mol) = ":'0',
                       "First ionization energy (kJ/mol)=":'906.4',
                       "Refractive_index = ": '1.00205',
                       "Speed_of_sound( m/s) = ": '3700',
                       "Latent heat of Fusion (KJ/mol)=":'7.35',
                       "Latent heat of Vapourization (kJ/mol)=":'119',
                       "Specific heat (J/kgK)=":'388',
                       "Thermal conductivity (W/m K)=":'120',
                       "Electronegetivity=":'1.65',
                       "Neutron cross-section (barn)=":'1.1'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Zn_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Ga_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ga_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ge_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ge_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def As_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,As_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Se_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Se_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Br_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Br_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
    
    
def Kr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Kr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Rb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Rb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Sr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
def Y_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Y_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()   
    
def Zr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Zr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()   
    
    

def Nb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Nb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Mo_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Mo_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Tc_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Tc_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
def Ru_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ru_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Rh_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Rh_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Pd_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pd_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
 
def Ag_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ag_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Cd_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cd_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def In_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,In_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Sn_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sn_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    

def Sb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Te_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Te_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()
    
def I_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,I_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Xe_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Xe_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Cs_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cs_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ba_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ba_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def La_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,La_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Ce_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ce_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Pr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Nd_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Nd_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Pm_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pm_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Sm_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sm_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Eu_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Eu_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Gd_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Gd_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Tb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Tb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Dy_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Dy_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ho_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ho_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Er_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Er_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Tm_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Tm_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Yb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Yb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Lu_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Lu_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Hf_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Hf_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ta_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ta_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def W_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,W_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Re_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Re_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Os_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Os_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ir_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ir_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Pt_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pt_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Au_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Au_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Hg_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Hg_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Tl_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Tl_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Pb_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pb_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Bi_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Bi_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Po_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Po_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def At_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,At_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Rn_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Rn_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Fr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Fr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ra_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ra_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Ac_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ac_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Th_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Th_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Pa_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pa_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def U_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,U_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()




def Np_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Np_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Pu_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Pu_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Am_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Am_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Cm_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cm_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Bk_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Bk_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Cf_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cf_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Es_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Es_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Fm_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Fm_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Md_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Md_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def No_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,No_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Lr_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Lr_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Rf_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Rf_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Db_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Db_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Sg_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Sg_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Bh_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Bh_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Hs_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Hs_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()

def Mt_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Mt_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()




def Ds_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ds_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Rg_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Rg_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()




def Cn_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Cn_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Nh_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Nh_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()




def Fl_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Fl_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Mc_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Mc_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Lv_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Lv_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()



def Ts_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Ts_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()


def Og_page():    
    global info
    info=Frame(root)
    info.grid(row=0,column=0)
    Name=Label(info,text='Lithium:')
    Name.config(font=("courier",24))
    Name.pack()
    Discovery=Label(info,text='(Discovery year : 1817)')
    Discovery.pack()
    basic_info=Label(info,text='Atomic no=3 , Group=1 ,Period=2 ,Block= S , CAS Number=7439-93-2')
    basic_info.config(font=("courier",12))
    basic_info.pack()
    content=Text(info,height=30,width=150,font=22)
    content.pack()
    
    content.insert(END,'PROPERTIES:-\n\n')
    atomic_properties={"Atomic_weight (g / mol) = ":'6.94' ,
                       "Oxidation_state = ":'[-1,+1]' ,
                       "Atomic_radius (pm)= ":'161',
                       "Covelent_radius(pm) = ":'128 (0.16%  error)' ,
                       "Van der waals radius (pm)=":'182',
                       "Boiling_point(Celcius) = " :'1342',
                       "Melting_point(Celcius) =":'180.54',
                       "Electron_affinity( kj / mol) = ":'59.6',
                       "First ionization energy (kJ/mol)=":'1312',
                       "Refractive_index = ": '1.000132',
                       "Speed_of_sound( m/s) = ": '1270',
                       "Latent heat of Fusion (KJ/mol)=":'0.558',
                       "Latent heat of Vapourization (kJ/mol)=":'0.452',
                       "Specific heat (J/kgK)=":'14300',
                       "Thermal conductivity (W/m K)=":'0.1805',
                       "Electronegetivity=":'2.2',
                       "Neutron cross-section (barn)=":'0.007'
                       }
    
    for prop in atomic_properties:
        content.insert(END,(prop+atomic_properties[prop]+'\n'))
    content.insert(END,'''

SUMMARY FROM WIKIPEDIA:-\n\n''')
    content.insert(END,Og_info)
    back=Button(info,text='Back',command=create_pt)
    back.pack()






           #This function destroys the main page of the periodic table which is common fr all the buttons
# def destroying_pt():
#     pt.destroy()

    
    
   
# this function is to create the periodic table after destruction
    # #function for creating periodic table
def create_pt():
    info.destroy()
    pt=Frame(root)
    pt.grid(row=0,column=0)

    H  = Button(pt,text='H',width=9,height=2,bg='blue',command=H_page)
    He = Button(pt,text='He',width=9,height=2,bg='blue',command=He_page)
    Li = Button(pt,text='Li',width=9,height=2,bg='silver',command=Li_page)
    Be = Button(pt,text='Be',width=9,height=2,bg='silver',command=Be_page)
    B  = Button(pt,text='B',width=9,height=2,bg='orange',command=B_page)
    C  = Button(pt,text='C',width=9,height=2,bg='blue',command=C_page)
    N  = Button(pt,text='N',width=9,height=2,bg='blue',command=N_page)
    O  = Button(pt,text='O',width=9,height=2,bg='blue',command=O_page)
    F  = Button(pt,text='F',width=9,height=2,bg='blue',command=F_page)
    Ne = Button(pt,text='Ne',width=9,height=2,bg='blue',command=Ne_page)
    Na = Button(pt,text='Na',width=9,height=2,bg='silver',command=Na_page)
    Mg = Button(pt,text='Mg',width=9,height=2,bg='silver',command=Mg_page)
    Al = Button(pt,text='Al',width=9,height=2,bg='silver',command=Al_page)
    Si = Button(pt,text='Si',width=9,height=2,bg='orange',command=Si_page)
    P  = Button(pt,text='P',width=9,height=2,bg='blue',command=P_page)
    S  = Button(pt,text='S',width=9,height=2,bg='blue',command=S_page)
    Cl = Button(pt,text='Cl',width=9,height=2,bg='blue',command=Cl_page)
    Ar = Button(pt,text='Ar',width=9,height=2,bg='blue',command=Ar_page)
    K  = Button(pt,text='K',width=9,height=2,bg='silver',command=K_page)
    Ca = Button(pt,text='Ca',width=9,height=2,bg='silver',command=Ca_page)
    Sc = Button(pt,text='Sc',width=9,height=2,bg='silver',command=Sc_page)
    Ti = Button(pt,text='Ti',width=9,height=2,bg='silver',command=Ti_page)
    V  = Button(pt,text='V',width=9,height=2,bg='silver',command=V_page)
    Cr = Button(pt,text='Cr',width=9,height=2,bg='silver',command=Cr_page)
    Mn = Button(pt,text='Mn',width=9,height=2,bg='silver',command=Mn_page)
    Fe = Button(pt,text='Fe',width=9,height=2,bg='silver',command=Fe_page)
    Co = Button(pt,text='Co',width=9,height=2,bg='silver',command=Co_page)
    Ni = Button(pt,text='Ni',width=9,height=2,bg='silver',command=Ni_page)
    Cu = Button(pt,text='Cu',width=9,height=2,bg='silver',command=Cu_page)
    Zn = Button(pt,text='Zn',width=9,height=2,bg='silver',command=Zn_page)
    Ga = Button(pt,text='Ga',width=9,height=2,bg='silver',command=Ga_page)
    Ge = Button(pt,text='Ge',width=9,height=2,bg='orange',command=Ge_page)
    As = Button(pt,text='As',width=9,height=2,bg='orange',command=As_page)
    Se = Button(pt,text='Se',width=9,height=2,bg='blue',command=Se_page)
    Br = Button(pt,text='Br',width=9,height=2,bg='blue',command=Br_page)
    Kr = Button(pt,text='Kr',width=9,height=2,bg='blue',command=Kr_page)
    Rb = Button(pt,text='Rb',width=9,height=2,bg='silver',command=Rb_page)
    Sr = Button(pt,text='Sr',width=9,height=2,bg='silver',command=Sr_page)
    Y  = Button(pt,text='Y',width=9,height=2,bg='silver',command=Y_page)
    Zr = Button(pt,text='Zr',width=9,height=2,bg='silver',command=Zr_page)
    Nb = Button(pt,text='Nb',width=9,height=2,bg='silver',command=Nb_page)
    Mo = Button(pt,text='Mo',width=9,height=2,bg='silver',command=Mo_page)
    Tc = Button(pt,text='Tc',width=9,height=2,command=Tc_page)#,bg='silver')
    Ru = Button(pt,text='Ru',width=9,height=2,bg='silver',command=Ru_page)
    Rh = Button(pt,text='Rh',width=9,height=2,bg='silver',command=Rh_page)
    Pd = Button(pt,text='Pd',width=9,height=2,bg='silver',command=Pd_page)
    Ag = Button(pt,text='Ag',width=9,height=2,bg='silver',command=Ag_page)
    Cd = Button(pt,text='Cd',width=9,height=2,bg='silver',command=Cd_page)
    In = Button(pt,text='In',width=9,height=2,bg='silver',command=In_page)
    Sn = Button(pt,text='Sn',width=9,height=2,bg='silver',command=Sn_page)
    Sb = Button(pt,text='Sb',width=9,height=2,bg='orange',command=Sb_page)
    Te = Button(pt,text='Te',width=9,height=2,bg='orange',command=Te_page)
    I  = Button(pt,text='I',width=9,height=2,bg='blue',command=I_page)
    Xe = Button(pt,text='Xe',width=9,height=2,bg='blue',command=Xe_page)
    Cs = Button(pt,text='Cs',width=9,height=2,bg='silver',command=Cs_page)
    Ba = Button(pt,text='Ba',width=9,height=2,bg='silver',command=Ba_page)
    La = Button(pt,text='La',width=9,height=2,bg='silver',command=La_page)
    Ce = Button(pt,text='Ce',width=9,height=2,bg='silver',command=Ce_page)
    Pr = Button(pt,text='Pr',width=9,height=2,bg='silver',command=Pr_page)
    Nd = Button(pt,text='Nd',width=9,height=2,bg='silver',command=Nd_page)
    Pm = Button(pt,text='Pm',width=9,height=2,command=Pm_page)#,bg='silver')
    Sm = Button(pt,text='Sm',width=9,height=2,bg='silver',command=Sm_page)
    Eu = Button(pt,text='Eu',width=9,height=2,bg='silver',command=Eu_page)
    Gd = Button(pt,text='Gd',width=9,height=2,bg='silver',command=Gd_page)
    Tb = Button(pt,text='Tb',width=9,height=2,bg='silver',command=Tb_page)
    Dy = Button(pt,text='Dy',width=9,height=2,bg='silver',command=Dy_page)
    Ho = Button(pt,text='Ho',width=9,height=2,bg='silver',command=Ho_page)
    Er = Button(pt,text='Er',width=9,height=2,bg='silver',command=Er_page)
    Tm = Button(pt,text='Tm',width=9,height=2,bg='silver',command=Tm_page)
    Yb = Button(pt,text='Yb',width=9,height=2,bg='silver',command=Yb_page)
    Lu = Button(pt,text='Lu',width=9,height=2,bg='silver',command=Lu_page)
    Hf = Button(pt,text='Hf',width=9,height=2,bg='silver',command=Hf_page)
    Ta = Button(pt,text='Ta',width=9,height=2,bg='silver',command=Ta_page)
    W  = Button(pt,text='W',width=9,height=2,bg='silver',command=W_page)
    Re = Button(pt,text='Re',width=9,height=2,bg='silver',command=Re_page)
    Os = Button(pt,text='Os',width=9,height=2,bg='silver',command=Os_page)
    Ir = Button(pt,text='Ir',width=9,height=2,bg='silver',command=Ir_page)
    Pt = Button(pt,text='Pt',width=9,height=2,bg='silver',command=Pt_page)
    Au = Button(pt,text='Au',width=9,height=2,bg='silver',command=Au_page)
    Hg = Button(pt,text='Hg',width=9,height=2,bg='silver',command=Hg_page)
    Tl = Button(pt,text='Tl',width=9,height=2,bg='silver',command=Tl_page)
    Pb = Button(pt,text='Pb',width=9,height=2,bg='silver',command=Pb_page)
    Bi = Button(pt,text='Bi',width=9,height=2,bg='silver',command=Bi_page)
    Po = Button(pt,text='Po',width=9,height=2,bg='orange',command=Po_page)
    At = Button(pt,text='At',width=9,height=2,bg='orange',command=At_page)
    Rn = Button(pt,text='Rn',width=9,height=2,bg='blue',command=Rn_page)
    Fr = Button(pt,text='Fr',width=9,height=2,bg='silver',command=Fr_page)
    Ra = Button(pt,text='Ra',width=9,height=2,bg='silver',command=Ra_page)
    Ac = Button(pt,text='Ac',width=9,height=2,bg='silver',command=Ac_page)
    Th = Button(pt,text='Th',width=9,height=2,bg='silver',command=Th_page)
    Pa = Button(pt,text='Pa',width=9,height=2,bg='silver',command=Pa_page)
    U  = Button(pt,text='U',width=9,height=2,bg='silver',command=U_page)
    Np = Button(pt,text='Np',width=9,height=2,command=Np_page)
    Pu = Button(pt,text='Pu',width=9,height=2,command=Pu_page)
    Am = Button(pt,text='Am',width=9,height=2,command=Am_page)
    Cm = Button(pt,text='Cm',width=9,height=2,command=Cm_page)
    Bk = Button(pt,text='Bk',width=9,height=2,command=Bk_page)
    Cf = Button(pt,text='Cf',width=9,height=2,command=Cf_page)
    Es = Button(pt,text='Es',width=9,height=2,command=Es_page)
    Fm = Button(pt,text='Fm',width=9,height=2,command=Fm_page)
    Md = Button(pt,text='Md',width=9,height=2,command=Md_page)
    No = Button(pt,text='No',width=9,height=2,command=No_page)
    Lr = Button(pt,text='Lr',width=9,height=2,command=Lr_page)
    Rf = Button(pt,text='Rf',width=9,height=2,command=Rf_page)
    Db = Button(pt,text='Db',width=9,height=2,command=Db_page)
    Sg = Button(pt,text='Sg',width=9,height=2,command=Sg_page)
    Bh = Button(pt,text='Bh',width=9,height=2,command=Bh_page)
    Hs = Button(pt,text='Hs',width=9,height=2,command=Hs_page)
    Mt = Button(pt,text='Mt',width=9,height=2,command=Mt_page)
    Ds = Button(pt,text='Ds',width=9,height=2,command=Ds_page)
    Rg = Button(pt,text='Rg',width=9,height=2,command=Rg_page)
    Cn = Button(pt,text='Cn',width=9,height=2,command=Cn_page)
    Nh = Button(pt,text='Nh',width=9,height=2,command=Nh_page)
    Fl = Button(pt,text='Fl',width=9,height=2,command=Fl_page)
    Mc = Button(pt,text='Mc',width=9,height=2,command=Mc_page)
    Lv = Button(pt,text='Lv',width=9,height=2,command=Lv_page)
    Ts = Button(pt,text='Ts',width=9,height=2,command=Ts_page)
    Og = Button(pt,text='Og',width=9,height=2,command=Og_page)
    #label for lanthanides
    Lanthanides=Label(pt,text="Lanthanides")
    Lanthanides.grid(row=9,column=3)
    #label for Actinides
    Actinides=Label(pt,text="Actinides")
    Actinides.grid(row=10,column=3)


    #showing all elements and buttons according to the group

    #space for upper row
    space_up=Label(pt,text="   ")
    space_up.grid(row=0,column=0)
    #sapce for left most column
    space_left=Label(pt,text="   ")
    space_left.grid(row=0,column=0)
    #1st group
    H.grid(row=1,column=1)
    Li.grid(row=2,column=1)
    Na.grid(row=3,column=1)
    K.grid(row=4,column=1)
    Rb.grid(row=5,column=1)
    Cs.grid(row=6,column=1)
    Fr.grid(row=7,column=1)
    #2nd group
    Be.grid(row=2,column=2)
    Mg.grid(row=3,column=2)
    Ca.grid(row=4,column=2)
    Sr.grid(row=5,column=2)
    Ba.grid(row=6,column=2)
    Ra.grid(row=7,column=2)
    #3rd group
    Sc.grid(row=4,column=3)
    Y.grid(row=5,column=3)
    #4th group
    Ti.grid(row=4,column=4)
    Zr.grid(row=5,column=4)
    Hf.grid(row=6,column=4)
    Rf.grid(row=7,column=4)
    #5th group
    V.grid(row=4,column=5)
    Nb.grid(row=5,column=5)
    Ta.grid(row=6,column=5)
    Db.grid(row=7,column=5)
    #6th group
    Cr.grid(row=4,column=6)
    Mo.grid(row=5,column=6)
    W.grid(row=6,column=6)
    Sg.grid(row=7,column=6)
    #7th group
    Mn.grid(row=4,column=7)
    Tc.grid(row=5,column=7)
    Re.grid(row=6,column=7)
    Bh.grid(row=7,column=7)
    #8th group
    Fe.grid(row=4,column=8)
    Ru.grid(row=5,column=8)
    Os.grid(row=6,column=8)
    Hs.grid(row=7,column=8)
    #9th group
    Co.grid(row=4,column=9)
    Rh.grid(row=5,column=9)
    Ir.grid(row=6,column=9)
    Mt.grid(row=7,column=9)
    #10th group
    Ni.grid(row=4,column=10)
    Pd.grid(row=5,column=10)
    Pt.grid(row=6,column=10)
    Ds.grid(row=7,column=10)
    #11th group
    Cu.grid(row=4,column=11)
    Ag.grid(row=5,column=11)
    Au.grid(row=6,column=11)
    Rg.grid(row=7,column=11)
    #12th group
    Zn.grid(row=4,column=12)
    Cd.grid(row=5,column=12)
    Hg.grid(row=6,column=12)
    Cn.grid(row=7,column=12)
    #13th group
    B.grid(row=2,column=13)
    Al.grid(row=3,column=13)
    Ga.grid(row=4,column=13)
    In.grid(row=5,column=13)
    Tl.grid(row=6,column=13)
    Nh.grid(row=7,column=13)
    #14th group
    C.grid(row=2,column=14)
    Si.grid(row=3,column=14)
    Ge.grid(row=4,column=14)
    Sn.grid(row=5,column=14)
    Pb.grid(row=6,column=14)
    Fl.grid(row=7,column=14)
    #15th group
    N.grid(row=2,column=15)
    P.grid(row=3,column=15)
    As.grid(row=4,column=15)
    Sb.grid(row=5,column=15)
    Bi.grid(row=6,column=15)
    Mc.grid(row=7,column=15)
    #16th group
    O.grid(row=2,column=16)
    S.grid(row=3,column=16)
    Se.grid(row=4,column=16)
    Te.grid(row=5,column=16)
    Po.grid(row=6,column=16)
    Lv.grid(row=7,column=16)
    #17th group
    F.grid(row=2,column=17)
    Cl.grid(row=3,column=17)
    Br.grid(row=4,column=17)
    I.grid(row=5,column=17)
    At.grid(row=6,column=17)
    Ts.grid(row=7,column=17)
    #18th group
    He.grid(row=1,column=18)
    Ne.grid(row=2,column=18)
    Ar.grid(row=3,column=18)
    Kr.grid(row=4,column=18)
    Xe.grid(row=5,column=18)
    Rn.grid(row=6,column=18)
    Og.grid(row=7,column=18)
    #for space at lanthanides
    space1=Label(pt,text="   ")
    space1.grid(row=8,column=2)
    #Lanthanides
    La.grid(row=9,column=4)
    Ce.grid(row=9,column=5)
    Pr.grid(row=9,column=6)
    Nd.grid(row=9,column=7)
    Pm.grid(row=9,column=8)
    Sm.grid(row=9,column=9)
    Eu.grid(row=9,column=10)
    Gd.grid(row=9,column=11)
    Tb.grid(row=9,column=12)
    Dy.grid(row=9,column=13)
    Ho.grid(row=9,column=14)
    Er.grid(row=9,column=15)
    Tm.grid(row=9,column=16)
    Yb.grid(row=9,column=17)
    Lu.grid(row=9,column=18)

    #Actinides
    Ac.grid(row=10,column=4)
    Th.grid(row=10,column=5)
    Pa.grid(row=10,column=6)
    U.grid(row=10,column=7)
    Np.grid(row=10,column=8)
    Pu.grid(row=10,column=9)
    Am.grid(row=10,column=10)
    Cm.grid(row=10,column=11)
    Bk.grid(row=10,column=12)
    Cf.grid(row=10,column=13)
    Es.grid(row=10,column=14)
    Fm.grid(row=10,column=15)
    Md.grid(row=10,column=16)
    No.grid(row=10,column=17)
    Lr.grid(row=10,column=18)













#First the buttons and the lables are created here

H  = Button(pt,text='H',width=9,height=2,bg='blue',command=H_page)
He = Button(pt,text='He',width=9,height=2,bg='blue',command=He_page)
Li = Button(pt,text='Li',width=9,height=2,bg='silver',command=Li_page)
Be = Button(pt,text='Be',width=9,height=2,bg='silver',command=Be_page)
B  = Button(pt,text='B',width=9,height=2,bg='orange',command=B_page)
C  = Button(pt,text='C',width=9,height=2,bg='blue',command=C_page)
N  = Button(pt,text='N',width=9,height=2,bg='blue',command=N_page)
O  = Button(pt,text='O',width=9,height=2,bg='blue',command=O_page)
F  = Button(pt,text='F',width=9,height=2,bg='blue',command=F_page)
Ne = Button(pt,text='Ne',width=9,height=2,bg='blue',command=Ne_page)
Na = Button(pt,text='Na',width=9,height=2,bg='silver',command=Na_page)
Mg = Button(pt,text='Mg',width=9,height=2,bg='silver',command=Mg_page)
Al = Button(pt,text='Al',width=9,height=2,bg='silver',command=Al_page)
Si = Button(pt,text='Si',width=9,height=2,bg='orange',command=Si_page)
P  = Button(pt,text='P',width=9,height=2,bg='blue',command=P_page)
S  = Button(pt,text='S',width=9,height=2,bg='blue',command=S_page)
Cl = Button(pt,text='Cl',width=9,height=2,bg='blue',command=Cl_page)
Ar = Button(pt,text='Ar',width=9,height=2,bg='blue',command=Ar_page)
K  = Button(pt,text='K',width=9,height=2,bg='silver',command=K_page)
Ca = Button(pt,text='Ca',width=9,height=2,bg='silver',command=Ca_page)
Sc = Button(pt,text='Sc',width=9,height=2,bg='silver',command=Sc_page)
Ti = Button(pt,text='Ti',width=9,height=2,bg='silver',command=Ti_page)
V  = Button(pt,text='V',width=9,height=2,bg='silver',command=V_page)
Cr = Button(pt,text='Cr',width=9,height=2,bg='silver',command=Cr_page)
Mn = Button(pt,text='Mn',width=9,height=2,bg='silver',command=Mn_page)
Fe = Button(pt,text='Fe',width=9,height=2,bg='silver',command=Fe_page)
Co = Button(pt,text='Co',width=9,height=2,bg='silver',command=Co_page)
Ni = Button(pt,text='Ni',width=9,height=2,bg='silver',command=Ni_page)
Cu = Button(pt,text='Cu',width=9,height=2,bg='silver',command=Cu_page)
Zn = Button(pt,text='Zn',width=9,height=2,bg='silver',command=Zn_page)
Ga = Button(pt,text='Ga',width=9,height=2,bg='silver',command=Ga_page)
Ge = Button(pt,text='Ge',width=9,height=2,bg='orange',command=Ge_page)
As = Button(pt,text='As',width=9,height=2,bg='orange',command=As_page)
Se = Button(pt,text='Se',width=9,height=2,bg='blue',command=Se_page)
Br = Button(pt,text='Br',width=9,height=2,bg='blue',command=Br_page)
Kr = Button(pt,text='Kr',width=9,height=2,bg='blue',command=Kr_page)
Rb = Button(pt,text='Rb',width=9,height=2,bg='silver',command=Rb_page)
Sr = Button(pt,text='Sr',width=9,height=2,bg='silver',command=Sr_page)
Y  = Button(pt,text='Y',width=9,height=2,bg='silver',command=Y_page)
Zr = Button(pt,text='Zr',width=9,height=2,bg='silver',command=Zr_page)
Nb = Button(pt,text='Nb',width=9,height=2,bg='silver',command=Nb_page)
Mo = Button(pt,text='Mo',width=9,height=2,bg='silver',command=Mo_page)
Tc = Button(pt,text='Tc',width=9,height=2,command=Tc_page)#,bg='silver')
Ru = Button(pt,text='Ru',width=9,height=2,bg='silver',command=Ru_page)
Rh = Button(pt,text='Rh',width=9,height=2,bg='silver',command=Rh_page)
Pd = Button(pt,text='Pd',width=9,height=2,bg='silver',command=Pd_page)
Ag = Button(pt,text='Ag',width=9,height=2,bg='silver',command=Ag_page)
Cd = Button(pt,text='Cd',width=9,height=2,bg='silver',command=Cd_page)
In = Button(pt,text='In',width=9,height=2,bg='silver',command=In_page)
Sn = Button(pt,text='Sn',width=9,height=2,bg='silver',command=Sn_page)
Sb = Button(pt,text='Sb',width=9,height=2,bg='orange',command=Sb_page)
Te = Button(pt,text='Te',width=9,height=2,bg='orange',command=Te_page)
I  = Button(pt,text='I',width=9,height=2,bg='blue',command=I_page)
Xe = Button(pt,text='Xe',width=9,height=2,bg='blue',command=Xe_page)
Cs = Button(pt,text='Cs',width=9,height=2,bg='silver',command=Cs_page)
Ba = Button(pt,text='Ba',width=9,height=2,bg='silver',command=Ba_page)
La = Button(pt,text='La',width=9,height=2,bg='silver',command=La_page)
Ce = Button(pt,text='Ce',width=9,height=2,bg='silver',command=Ce_page)
Pr = Button(pt,text='Pr',width=9,height=2,bg='silver',command=Pr_page)
Nd = Button(pt,text='Nd',width=9,height=2,bg='silver',command=Nd_page)
Pm = Button(pt,text='Pm',width=9,height=2,command=Pm_page)#,bg='silver')
Sm = Button(pt,text='Sm',width=9,height=2,bg='silver',command=Sm_page)
Eu = Button(pt,text='Eu',width=9,height=2,bg='silver',command=Eu_page)
Gd = Button(pt,text='Gd',width=9,height=2,bg='silver',command=Gd_page)
Tb = Button(pt,text='Tb',width=9,height=2,bg='silver',command=Tb_page)
Dy = Button(pt,text='Dy',width=9,height=2,bg='silver',command=Dy_page)
Ho = Button(pt,text='Ho',width=9,height=2,bg='silver',command=Ho_page)
Er = Button(pt,text='Er',width=9,height=2,bg='silver',command=Er_page)
Tm = Button(pt,text='Tm',width=9,height=2,bg='silver',command=Tm_page)
Yb = Button(pt,text='Yb',width=9,height=2,bg='silver',command=Yb_page)
Lu = Button(pt,text='Lu',width=9,height=2,bg='silver',command=Lu_page)
Hf = Button(pt,text='Hf',width=9,height=2,bg='silver',command=Hf_page)
Ta = Button(pt,text='Ta',width=9,height=2,bg='silver',command=Ta_page)
W  = Button(pt,text='W',width=9,height=2,bg='silver',command=W_page)
Re = Button(pt,text='Re',width=9,height=2,bg='silver',command=Re_page)
Os = Button(pt,text='Os',width=9,height=2,bg='silver',command=Os_page)
Ir = Button(pt,text='Ir',width=9,height=2,bg='silver',command=Ir_page)
Pt = Button(pt,text='Pt',width=9,height=2,bg='silver',command=Pt_page)
Au = Button(pt,text='Au',width=9,height=2,bg='silver',command=Au_page)
Hg = Button(pt,text='Hg',width=9,height=2,bg='silver',command=Hg_page)
Tl = Button(pt,text='Tl',width=9,height=2,bg='silver',command=Tl_page)
Pb = Button(pt,text='Pb',width=9,height=2,bg='silver',command=Pb_page)
Bi = Button(pt,text='Bi',width=9,height=2,bg='silver',command=Bi_page)
Po = Button(pt,text='Po',width=9,height=2,bg='orange',command=Po_page)
At = Button(pt,text='At',width=9,height=2,bg='orange',command=At_page)
Rn = Button(pt,text='Rn',width=9,height=2,bg='blue',command=Rn_page)
Fr = Button(pt,text='Fr',width=9,height=2,bg='silver',command=Fr_page)
Ra = Button(pt,text='Ra',width=9,height=2,bg='silver',command=Ra_page)
Ac = Button(pt,text='Ac',width=9,height=2,bg='silver',command=Ac_page)
Th = Button(pt,text='Th',width=9,height=2,bg='silver',command=Th_page)
Pa = Button(pt,text='Pa',width=9,height=2,bg='silver',command=Pa_page)
U  = Button(pt,text='U',width=9,height=2,bg='silver',command=U_page)
Np = Button(pt,text='Np',width=9,height=2,command=Np_page)
Pu = Button(pt,text='Pu',width=9,height=2,command=Pu_page)
Am = Button(pt,text='Am',width=9,height=2,command=Am_page)
Cm = Button(pt,text='Cm',width=9,height=2,command=Cm_page)
Bk = Button(pt,text='Bk',width=9,height=2,command=Bk_page)
Cf = Button(pt,text='Cf',width=9,height=2,command=Cf_page)
Es = Button(pt,text='Es',width=9,height=2,command=Es_page)
Fm = Button(pt,text='Fm',width=9,height=2,command=Fm_page)
Md = Button(pt,text='Md',width=9,height=2,command=Md_page)
No = Button(pt,text='No',width=9,height=2,command=No_page)
Lr = Button(pt,text='Lr',width=9,height=2,command=Lr_page)
Rf = Button(pt,text='Rf',width=9,height=2,command=Rf_page)
Db = Button(pt,text='Db',width=9,height=2,command=Db_page)
Sg = Button(pt,text='Sg',width=9,height=2,command=Sg_page)
Bh = Button(pt,text='Bh',width=9,height=2,command=Bh_page)
Hs = Button(pt,text='Hs',width=9,height=2,command=Hs_page)
Mt = Button(pt,text='Mt',width=9,height=2,command=Mt_page)
Ds = Button(pt,text='Ds',width=9,height=2,command=Ds_page)
Rg = Button(pt,text='Rg',width=9,height=2,command=Rg_page)
Cn = Button(pt,text='Cn',width=9,height=2,command=Cn_page)
Nh = Button(pt,text='Nh',width=9,height=2,command=Nh_page)
Fl = Button(pt,text='Fl',width=9,height=2,command=Fl_page)
Mc = Button(pt,text='Mc',width=9,height=2,command=Mc_page)
Lv = Button(pt,text='Lv',width=9,height=2,command=Lv_page)
Ts = Button(pt,text='Ts',width=9,height=2,command=Ts_page)
Og = Button(pt,text='Og',width=9,height=2,command=Og_page)
#label for lanthanides
Lanthanides=Label(pt,text="Lanthanides")
Lanthanides.grid(row=9,column=3)
#label for Actinides
Actinides=Label(pt,text="Actinides")
Actinides.grid(row=10,column=3)


#showing all elements and buttons according to the group

#space for upper row
space_up=Label(pt,text="   ")
space_up.grid(row=0,column=0)
#sapce for left most column
space_left=Label(pt,text="   ")
space_left.grid(row=0,column=0)
#1st group
H.grid(row=1,column=1)
Li.grid(row=2,column=1)
Na.grid(row=3,column=1)
K.grid(row=4,column=1)
Rb.grid(row=5,column=1)
Cs.grid(row=6,column=1)
Fr.grid(row=7,column=1)
#2nd group
Be.grid(row=2,column=2)
Mg.grid(row=3,column=2)
Ca.grid(row=4,column=2)
Sr.grid(row=5,column=2)
Ba.grid(row=6,column=2)
Ra.grid(row=7,column=2)
#3rd group
Sc.grid(row=4,column=3)
Y.grid(row=5,column=3)
#4th group
Ti.grid(row=4,column=4)
Zr.grid(row=5,column=4)
Hf.grid(row=6,column=4)
Rf.grid(row=7,column=4)
#5th group
V.grid(row=4,column=5)
Nb.grid(row=5,column=5)
Ta.grid(row=6,column=5)
Db.grid(row=7,column=5)
#6th group
Cr.grid(row=4,column=6)
Mo.grid(row=5,column=6)
W.grid(row=6,column=6)
Sg.grid(row=7,column=6)
#7th group
Mn.grid(row=4,column=7)
Tc.grid(row=5,column=7)
Re.grid(row=6,column=7)
Bh.grid(row=7,column=7)
#8th group
Fe.grid(row=4,column=8)
Ru.grid(row=5,column=8)
Os.grid(row=6,column=8)
Hs.grid(row=7,column=8)
#9th group
Co.grid(row=4,column=9)
Rh.grid(row=5,column=9)
Ir.grid(row=6,column=9)
Mt.grid(row=7,column=9)
#10th group
Ni.grid(row=4,column=10)
Pd.grid(row=5,column=10)
Pt.grid(row=6,column=10)
Ds.grid(row=7,column=10)
#11th group
Cu.grid(row=4,column=11)
Ag.grid(row=5,column=11)
Au.grid(row=6,column=11)
Rg.grid(row=7,column=11)
#12th group
Zn.grid(row=4,column=12)
Cd.grid(row=5,column=12)
Hg.grid(row=6,column=12)
Cn.grid(row=7,column=12)
#13th group
B.grid(row=2,column=13)
Al.grid(row=3,column=13)
Ga.grid(row=4,column=13)
In.grid(row=5,column=13)
Tl.grid(row=6,column=13)
Nh.grid(row=7,column=13)
#14th group
C.grid(row=2,column=14)
Si.grid(row=3,column=14)
Ge.grid(row=4,column=14)
Sn.grid(row=5,column=14)
Pb.grid(row=6,column=14)
Fl.grid(row=7,column=14)
#15th group
N.grid(row=2,column=15)
P.grid(row=3,column=15)
As.grid(row=4,column=15)
Sb.grid(row=5,column=15)
Bi.grid(row=6,column=15)
Mc.grid(row=7,column=15)
#16th group
O.grid(row=2,column=16)
S.grid(row=3,column=16)
Se.grid(row=4,column=16)
Te.grid(row=5,column=16)
Po.grid(row=6,column=16)
Lv.grid(row=7,column=16)
#17th group
F.grid(row=2,column=17)
Cl.grid(row=3,column=17)
Br.grid(row=4,column=17)
I.grid(row=5,column=17)
At.grid(row=6,column=17)
Ts.grid(row=7,column=17)
#18th group
He.grid(row=1,column=18)
Ne.grid(row=2,column=18)
Ar.grid(row=3,column=18)
Kr.grid(row=4,column=18)
Xe.grid(row=5,column=18)
Rn.grid(row=6,column=18)
Og.grid(row=7,column=18)
#for space at lanthanides
space1=Label(pt,text="   ")
space1.grid(row=8,column=2)
#Lanthanides
La.grid(row=9,column=4)
Ce.grid(row=9,column=5)
Pr.grid(row=9,column=6)
Nd.grid(row=9,column=7)
Pm.grid(row=9,column=8)
Sm.grid(row=9,column=9)
Eu.grid(row=9,column=10)
Gd.grid(row=9,column=11)
Tb.grid(row=9,column=12)
Dy.grid(row=9,column=13)
Ho.grid(row=9,column=14)
Er.grid(row=9,column=15)
Tm.grid(row=9,column=16)
Yb.grid(row=9,column=17)
Lu.grid(row=9,column=18)

#Actinides
Ac.grid(row=10,column=4)
Th.grid(row=10,column=5)
Pa.grid(row=10,column=6)
U.grid(row=10,column=7)
Np.grid(row=10,column=8)
Pu.grid(row=10,column=9)
Am.grid(row=10,column=10)
Cm.grid(row=10,column=11)
Bk.grid(row=10,column=12)
Cf.grid(row=10,column=13)
Es.grid(row=10,column=14)
Fm.grid(row=10,column=15)
Md.grid(row=10,column=16)
No.grid(row=10,column=17)
Lr.grid(row=10,column=18)
    
# def hydrogen():
#     destroying_pt()
#create_pt()    
    
    
    


#main loop
root.mainloop()

