#!c:\Tcl\bin\tclsh

mol new protein_ligand.gro
mol addfile final_production.xtc first 0 last -1 step 1 waitfor all

file mkdir saltbridges
package require saltbr
saltbr -sel [atomselect top all] -log saltbridges.log -outdir ./saltbridges

