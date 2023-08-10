# e-Reader Decompiler and Compression Tools
This code, originally started by [RollingStar](https://github.com/RollingStar/CardShark), is designed to work in combination with tools created by CaitSith2 and Tim Schuerewegen in order to decompile and re-compress Nintendo's e-Reader card data for the Game Boy Advance.


## Important Information
These tools are designed **specifically for use with Animal Crossing e-Reader cards**. Other e-Reader cards exist, such as those for Mario Party and Pokémon, but as of right now this tool is formatted for Animal Crossing only. As it is possible to update this tool in the future to incorporate other games, I've left the project name as-is to remain general. 

Further, these tools are merely assists that automate processes and make the effort of modifying e-Reader data less troublesome. That is to say, while these tools do decode fully automatically, these tools **do not** accurately replicate HAL Laboratory's `vpk0` compression methods when encoding. This is because HAL's specific compression settings are not known. Nevertheless, it is still possible to get e-Reader card data to read properly through clever manual editing of specific e-Reader header data, which is detailed in the tutorial. In theory, this process could be automated for specific card data, but there are too many e-Reader cards with differing flags and data to make it worth writing automation to detect each type. Regardless, if only interested in modifying Animal Crossing e-Reader card data, these tools are still essential for the process to work. 


## Requirements
These tools are part of a larger project detailed in this tutorial, where more requirements are necessary for editing the files. However, for these tools specifically for decoding/encoding only, you will need:

- Windows 10 or higher (no Mac or Linux, sorry)
- Python 3
- [CaitSith2's Dot Dode Dev Package](https://www.caitsith2.com/ereader/devtools.htm)
- Access to e-Reader card data in `.raw` format


## Workflow
**IMPORTANT:** *The code hosted here is part of a larger project designed to allow users to modify decompressed e-Reader card data. Without following this larger tutorial, these tools merely decode and encode e-Reader data through specific file-structures without explaining how to do much with them.* 

 1. Clone the Git repository to a new folder of your choosing.
 2. Enter the folder `/eReader-Compression/`. This will be your root folder.
 3. Download and extract [CaitSith2's Dot Dode Dev Package](https://www.caitsith2.com/ereader/devtools.htm) to the root folder.
 4. Your root folder should now contain several new files, but you can delete all the new files **except**  `nedcenc.exe`, `nedclib.dll`, and `nevpk.exe`. Alternatively, you can download these separately from CaitSith2's site and put them in the root folder.
 5. Place your `.raw` e-Reader card data in the `/cards/raw/` folder.
 6. Run `raw-to-bin.bat` to automatically decode the `.raw` files in said folder into `.bin`. These new `.bin` files are placed in `/cards/bin/`.
 7. Run `bin_to_vpk.py` to automatically decode the `.bin` files into separate `.header` and `.vpk` chunks. These files are placed in `/cards/vpk/`
 8. Run `vpk-to-dec.bat` to automatically decode the `.vpk` chunks into readable, decompressed you can modify with a hex editor.
 9. When finished modifying, run `dec-to-vpk.bat` and `vpk-to-bin.py` to compress through the files back to `.bin`. This will overwrite the original files in the folder.
 10. Run `bin-to-raw.bat` to convert back to `.raw` for use in e-Reader scanning or dot code printing. 


## Known Bugs
- The code will occasionally fail to decode when dealing with multiple `.raw` files. I recommend doing one at a time for now.


## Acknowledgements
Huge thanks to [RollingStar](https://github.com/RollingStar/CardShark) for starting this project and giving me the motivation to finish it. A large portion of this codebase belongs to them.

