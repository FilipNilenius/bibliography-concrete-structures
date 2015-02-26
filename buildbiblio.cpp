// c++ implementation of concrete structure's bibliography
// written by Filip Nilenius, 2014-06-03

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
using namespace std;


int main ()
{
    // delete old pdfs
    system("del *.pdf");

    // setup different typefaces
    string typeFaceName[] = {"computermodern","times","ebgaramond","palatino"};
    string typeFaceSyntax[] = {" ","\\usepackage{mathptmx}","\\usepackage{ebgaramond}","\\usepackage[sc]{mathpazo}"};

    // for all typefaces
    for(int n=0;n<4;++n){
        std::ifstream ifs("biblio.tex");
        std::string line;
        std::ofstream out("output.tex");
        while(std::getline(ifs, line))
        {
            if(line=="%stringtobereplacedbyfontsyntax"){
                out << typeFaceSyntax[n] <<'\n';
            }
            else{
                out << line <<'\n';
            }
        }
        out.close();

        // system calls to compile pdfs
        system("pdflatex output");
        if(n==0){ // only necessary first time
            system("biber output");
            system("pdflatex output");
        }
        system("pdflatex output");

        // rename pdf according to its typeface name
        string newName = "biblio_";
        newName.append(typeFaceName[n]);
        newName.append(".pdf");
        rename("output.pdf",newName.c_str());
        system("del output.tex");

    }
    // clean up
    system("del output.*");
    return 0;
}
