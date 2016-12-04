# CyberSecurity_Strategies
Machine-based Text Analytics of CyberSecurity Strategies

The cybersecurity strategies can be downloaded from this website from the International Telecommunications Union:

[National Cybersecurity Strategies repository](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/National-Strategies-repository.aspx)  

Here you can see a human analysis of cyberscurity laws. It would be interesting to see whether a similar analysis per country could be done using machine-learning or other text mining techniques:

[Cyberwellness Profiles](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/Country_Profiles.aspx)

## Suggested analysis

###Text mining

- Create a text version of each of the cybersecurity strategy documents at the link above
- Break down each document into sentences 
- Classify each sentence and try to assign it a tagg from this list below. It is expected that each document will have hundreds or thousands of sentences tagged and many sentences which can't be tagged because they are note related to any of the taggs below.

**These labels come from the headers in the cyberwellness profiles linked above**
| Category               | Sub category |
|------------------------| -------------|
|LEGAL MEASURES          | CRIMINAL LEGISLATION, REGULATION AND COMPLIANCE|
|TECHNICAL MEASURES      | CIRT, STANDARDS, CERTIFICATION|
|ORGANIZATION MEASURES   | POLICY, ROADMAP FOR GOVERNANCE, RESPONSIBLE AGENCY, NATIONAL BENCHMARKING|
|CAPACITY BUILDING       | STANDARDISATION DEVELOPMENT, MANPOWER DEVELOPMENT, PROFESSIONAL CERTIFICATION, AGENCY CERTIFICATION|
|COOPERATION             | INTRA-STATE COOPERATION, INTRA-AGENCY COOPERATION, PUBLIC SECTOR PARTNERSHIP,  INTERNATIONAL COOPERATION|
|CHILD ONLINE PROTECTION | NATIONAL LEGISLATION,  UN CONVENTION AND PROTOCOL, INSTITUTIONAL SUPPORT, REPORTING MECHANISM|

>For example, let's classify an imaginary sentence from imaginary country Astlan:  
>"This country has implemented strict criminal legislation and certification of technology specialists for cybersecurity"  

- A suggested schema to store this sentence after the analysis is: (suggested json or yaml format):

Sentence id number: 10384648  
Source Document: "Astlan Cyber Security Strategy 2016.pdf"  
Country: "Astlan"  
Sentence: "This country has implemented strict criminal legislation and certification of technology specialists for cybersecurity"  
Taggs: "Legal - Criminal legislation", "Technical measures - certification"  
Sentence Position in Document: page #, or byte   (this is so then we can link to the sentence)

- The above shuold be done for each of the 73 CyberSecurity strategies  

### Search (optional but very useful)
If you used a search engine for any of the steps above this information is unecessary to you, but if you did not, keep reading:  
- If the thousands of sentences in the documents could be ingested into an Apache Solr or Elastic Search server they could be asily searched by the end-users with their specific queries. (You might be able to leverage built-in features to do similarity queries, etc.)

## Expected result
After all your efforts above, the expected product is a web page where end-users can interact with the data. The webpage should include:

- A visualization where the user can graphically explore the dataset
- It must include an area where the user can read the tagged sentences
- It must have buttons or check boxes to filter the sentences displayed (Country, Source Document, Taggs). Multiple filters should be allowed simultaneously. (E.g. Filter by country and by 2 taggs)
- Ideally the users shuld be able to query the dataset freely.

### Examples

**This example interface includes a search engine and a rich visualization** https://unite.un.org/ideas/content/whs-explorer  
**This example project performed all the analysis offline and just created a visualization of the results**  
https://unite.un.org/ideas/content/links-sustainable-cities

