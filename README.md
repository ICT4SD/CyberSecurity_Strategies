# CyberSecurity_Strategies
Machine-based Text Analytics of CyberSecurity Strategies

The cybersecurity strategies can be downloaded from this website from the International Telecommunications Union:

[National Cybersecurity Strategies repository](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/National-Strategies-repository.aspx)  

Here you can see a human analysis of cyberscurity laws. It would be interesting to see whether a similar analysis per country could be done using machine-learning or other text mining techniques:

[Cyberwellness Profiles](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/Country_Profiles.aspx)

## Suggested analysis

###Text mining

- Create a text version of the cybersecurity document  
- Extract each sentence for each document  
- Tagg each sentence with labels such as (LEGAL MEASURES: CRIMINAL LEGISLATION, REGULATION AND COMPLIANCE, TECHNICAL MEASURES: CIRT, STANDARDS, CERTIFICATION, etc.)  **These labels come from the headers in the cyberwellness profiles linked above**  
Each document will have hundreds or thousands of sentences tagged. 

- Each resulting sentence could be stored with these attributes (suggested json or yaml format):

Sentence id number: 10384648  
Source Document: "Cyber Security Strategy 2016.pdf"  
Country: "Country name"  
Sentence: "This country has implemented strict criminal legislation to prevent that certification of specialists is not occuring"  
Taggs: "Criminal legislation", "certification"  
Sentence Position in Document: page #, or byte   (this is so then we can link to the sentence)  

- The above shuold be done for each of the 73 CyberSecurity strategies  

### Visualization
- Create a visualization where the user can view the dataset built above graphically
- It must include areas to read the sentences
- Buttons or check boxes to filter the sentences displayed (Country, Source Document, Taggs). Multiple filters should be allowed simultaneously. (E.g. Filter by country and by 2 taggs)

### Search (optional but very useful)
If you used a search engine for the process above then this information is redundant, but if you did not, keep reading:  
- If the thousands of sentences in the documents could be ingested into an Apache Solr or Elastic Search server they could be asily searched by the end-users with their specific queries.

**This example interface includes a search engine and a rich visualization** https://unite.un.org/ideas/content/whs-explorer

**This example project performed all the analysis offline and just created a visualization of the results**
https://unite.un.org/ideas/content/links-sustainable-cities




