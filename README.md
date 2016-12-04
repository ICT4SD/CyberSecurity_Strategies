# CyberSecurity_Strategies
Machine-based Text Analytics of CyberSecurity Strategies

The cybersecurity strategies can be downloaded from this website from the International Telecommunications Union:

[National Cybersecurity Strategies repository](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/National-Strategies-repository.aspx)  

Here you can see a human analysis of cyberscurity laws. It would be interesting to see whether a similar analysis per country could be done using machine-learning or other text mining techniques:

[Cyberwellness Profiles](http://www.itu.int/en/ITU-D/Cybersecurity/Pages/Country_Profiles.aspx)

## Suggested analysis

> Create a text version of the cybersecurity document  
> Extract each sentence for each document  
> Tagg each sentence with labels such as (LEGAL MEASURES: CRIMINAL LEGISLATION, REGULATION AND COMPLIANCE, TECHNICAL MEASURES: CIRT, STANDARDS, CERTIFICATION, etc.)  **These labels come from the headers in the cyberwellness profiles linked above**  
Each document will have hundreds or thousands of sentences tagged.  
> Each resulting sentence could be stored with these attributes (suggested json or yaml format):

Sentence id number: 10384648
SourceDocument: "Cyber Security Strategy 2016.pdf"
Country: "Country name"
Sentence: "This country has implemented strict criminal legislation to prevent that certification of specialists is not occuring"
taggs: "Criminal legislation", "certification"
sentencePositionInDocument: page #, or byte   (this is so then we can link to the sentence)

> The above shuold be done for each of the 73 CyberSecurity strategies  



