mol new protein_ligand.gro 
mol addfile final_production.xtc first 0 last -1 waitfor all

package require hbonds
#hbonds -sel1 [atomselect top "protein and resid 1"] -sel2 [atomselect top "not protein"]  -writefile yes -plot no 
file mkdir hbonds

for {set i 1} {$i  < 308} {incr i} {
	set string1 "protein and resid "
	set string2 $i
	set string3 ".dat"
	#set
	set selection_1 [concat $string1 $string2]
	#puts $selection_1
	set file_name [concat $string2 $string3] 
	hbonds -sel1 [atomselect top $selection_1] -sel2 [atomselect top "not protein"]	-writefile yes -outfile $i.dat -plot no -outdir ./hbonds
}

