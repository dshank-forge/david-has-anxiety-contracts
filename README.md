# david-has-anxiety-contracts

Bookmark: Getting art_metadata.py to import correctly into upload_to_pinata.py

TODO: 
1. Upload metadata to IPFS 
   1. Use upload_to_pinata.py in nft-demo 
   2. Upload image to IPFS, note URI
   3. Upload JSON to IPFS, which will include image URI
2. Identify URIs of artwork on IPFS
3. Figure out how front-end app can call the smart contract mint function using that correct URI
4. Implement an "ownerCount" function that keeps track of how many people have owned each token, so that first x owners can cash in "30 mins with Dave"

Questions:
1. How much energy does one tx on this contract use?
2. I know how to upload an image file, but how do I upload a metadata file? -- Same way!