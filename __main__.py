import streamlit as st

# Titles
st.subheader("HI! I AM RESUME CREATOR!!!")
st.subheader("HOW CAN I HELP YOU?")
st.subheader("I WILL GENERATE A RESUME BASED ON THE IT FIELD!")
st.subheader("ASK YOUR QUESTIONS!")

# Function to fetch resume based on role
def load_state(role, name):
    role = role.lower()  # Convert role to lowercase for consistency

    if role == "software developer":
        return f"""
### Resume for Software Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "full-stack developer":
        return f"""
### Resume for Full-Stack Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Objective:
- To deliver seamless user experiences through full-stack web development.

#### Skills:
- Proficient in React, Node.js, and MongoDB
- Experience with RESTful APIs and GraphQL
- Skilled in CI/CD pipelines

#### Experience:
- Built end-to-end e-commerce solutions at ABC Inc.
- Improved page load speed by 40%

#### Education:
- Bachelor of Computer Engineering

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "product manager":
        return f"""
### Resume for Product Manager:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Objective:
- To strategize and manage the product lifecycle to deliver exceptional customer value.
- Motivated and detail-oriented IT professional with a strong foundation in system administration, cloud computing, and software development.
- Seeking an opportunity to leverage my expertise in key areas such as network management, cybersecurity, or application development to drive innovative solutions.

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    

    elif role == "blockchain developer":
        return f"""Resume for Blockchain Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""


    elif role == "iot specialist":
        return f"""Resume for IoT Specialist:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
""" 
    elif role == "front-end developer":
        return f"""Resume for Front-End Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""

    elif role == "back-end developer":
        return f"""Resume for Back-End Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "mobile app developer":
        return f"""Resume for Mobile App Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    
    elif role == "devops engineer":
        return f"""Resume for DevOps Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "game developer":
        return f"""Resume for Game Developer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "embedded systems engineer":
        return f"""Resume for Embedded Systems Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "quality assurance engineer":
        return f"""Resume for Quality Assurance Engineer:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "software architect":
        return f"""Resume for Software Architect:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    
    elif role == "data analyst":
        return f"""Resume for Data Analyst:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    
    elif role == "data engineer":
        return f"""Resume for Data Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "machine learning engineer":
        return f"""Resume for Machine Learning Engineer:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "ai specialist":
        return f"""Resume for AI Specialist:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    
    elif role == "business intelligence analyst":
        return f"""Resume for Business Intelligence Analyst:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    
    elif role == "data scientists":
        return f"""Resume for Data Scientist:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "cybersecurity analyst":
        return f"""Resume for Cybersecurity Analyst:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""

    elif role == "cloud engineer":
        return f"""Resume for Cloud Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "penetration tester":
        return f"""Resume for Penetration Tester:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "network engineer":
        return f"""Resume for Network Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "data scientist":
        return f"""Resume for Data Scientist:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""

    elif role == "security architect":
        return f"""Resume for Security Architect:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "system administrator":
        return f"""Resume for System Administrator:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "database administrator":
        return f"""Resume for Database Administrator:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "it support specialist":
        return f"""Resume for IT Support Specialist:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""

    elif role == "site reliability engineer":
        return f"""Resume for Site Reliability Engineer:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""


    elif role == "scrum master":
        return f"""Resume for Scrum Master:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "it project manager":
        return f"""Resume for IT Project Manager:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "product manager":
        return f"""Resume for Product Manager:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "blockchain developer":
        return f"""Resume for Blockchain Developer:
**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    elif role == "iot specialist":
        return f"""Resume for IoT Specialist:

**Name**: {name}  
**LinkedIn**: [Your LinkedIn URL]  
**Email**: [Your Email]  
**Address**: [Your Address]  
**Phone**: [Your Phone Number]  

#### Professional Summary:
- Innovative and detail-oriented Software Developer with 1.8 years of experience in UI/UX design, web development, and front-end engineering.
- Adept at building user-centric applications and delivering seamless user experiences.
- Proficient in modern development frameworks and passionate about solving complex problems with clean and efficient code.
- Currently seeking an opportunity to contribute to cutting-edge projects in a dynamic environment.

#### Technical Skills:
- **Programming Languages**: JavaScript, Python, HTML, CSS, Java
- **Frameworks & Libraries**: React.js, Node.js, Bootstrap, Tailwind CSS
- **Tools**: Figma, Adobe XD, Git, VS Code
- **Databases**: MySQL, MongoDB
- **Other Skills**: Responsive Design, Cross-Browser Compatibility, Debugging

#### Work Experience:
**UI/UX Designer & Developer**  
*ACCENTURE, Location: Chennai*  
*March 2014 - Present*
- Designed and developed responsive user interfaces using HTML, CSS, and JavaScript.
- Implemented React components to enhance interactivity and scalability.
- Optimized web applications for speed and scalability, improving load times by 30%.
- Collaborated with cross-functional teams to align technical implementations with business goals.

**Front-End Developer**  
*ACCENTURE, Location: Chennai*  
*April 2014 - January 2016*
- Built dynamic web applications with React.js and integrated RESTful APIs.
- Enhanced application performance and accessibility to achieve WCAG compliance.
- Led debugging and testing processes, reducing bugs by 25%.

#### Education:
- **Bachelor of Technology in Computer Science Engineering**  
  *Anna University, Location: Chennai*  
  *March 2009 - April 2014*

#### Certifications:
- Full-Stack Web Development Certification – (2012)
- UI/UX Design Certification – (2015)

#### Projects:
- **Portfolio Website**: Designed and developed a personal portfolio showcasing projects and achievements using React.js and Tailwind CSS.
- **Travel Blog Website**: Created a responsive travel blog platform featuring user authentication, post creation, and comment functionality.
- **E-commerce Application**: Built a fully functional e-commerce platform with cart, payment gateway, and product catalog.

#### Interests:
- Exploring emerging technologies
- Contributing to open-source projects
- Traveling and blogging
"""
    else:
        return "Resume not available for the specified role."

# Input user details
name = st.text_input("Enter your name: ")
role = st.text_input("Enter your role based on IT field: ")

# Fetch and display the resume when both inputs are provided
if name and role:
    resume = load_state(role, name)
    st.write(f"Hello, {name}!")
    st.markdown(resume)  # Use markdown to display the resume with bullet points
else:
    st.write("Please enter your name and role to generate the resume.")
