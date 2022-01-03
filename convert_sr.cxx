
//C++
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <math.h>

//Boost
#include <boost/tokenizer.hpp>
#include <boost/program_options.hpp>

//HepMC3
#include "HepMC3/GenEvent.h"
#include "HepMC3/GenVertex.h"
#include "HepMC3/GenParticle.h"
#include "HepMC3/WriterAscii.h"

using namespace std;
using namespace boost;
using namespace HepMC3;

//functions
map<string, int> get_header(ifstream &in);

//_____________________________________________________________________________
int main(int argc, char* argv[]) {

  //command line arguments
  program_options::options_description opt("Program options");
  opt.add_options()("input,i", program_options::value<string>(), "SR input");
  opt.add_options()("output,o", program_options::value<string>(), "HepMC3 output");
  opt.add_options()("nev,n", program_options::value<long>(), "Number of events");
  opt.add_options()("invert_z", program_options::value<bool>(), "Inversion along z axis");

  program_options::variables_map opt_map;
  program_options::store(program_options::parse_command_line(argc, argv, opt), opt_map);

  //SR input
  string input = "../../input/25098.csv";
  if( opt_map.count("input") ) {
    input = opt_map["input"].as<string>();
  }
  ifstream in(input);

  //HepMC3 output
  string output = "sr.hepmc";
  if( opt_map.count("output") ) {
    output = opt_map["output"].as<string>();
  }
  std::shared_ptr<GenRunInfo> run = std::make_shared<GenRunInfo>();
  WriterAscii file(output, run);

  //inversion in z axis
  int invert_z = 1;
  if( opt_map.count("invert_z") and opt_map["invert_z"].as<bool>() ) {
    invert_z = -1;
  }

  //input header
  map<string, int> header = get_header(in);

  //indices in the input
  int idirx = header["Dir_X"];
  int idiry = header["Dir_Y"];
  int idirz = header["Dir_Z"];
  int ien = header["Energy_[eV]"];
  int iposx = header["Pos_X_[cm]"];
  int iposy = header["Pos_Y_[cm]"];
  int iposz = header["Pos_Z_[cm]"];
  int iflux = header["Flux_[photon/s]"];
  int ipower = header["Power_[W]"];

  //input loop
  long iev = 0; // line index
  long nmax = -1; // maximal number of events
  if( opt_map.count("nev") ) {
    nmax = opt_map["nev"].as<long>();
  }
  string line; // read line
  int lsiz = header.size(); // num of values in line
  vector<double> val(lsiz); // values in line
  char_separator<char> sep(","); // for tokenizer
  while( getline(in, line) ) {
    if( ++iev > nmax and nmax >= 0 ) break;

    //split the line
    tokenizer< char_separator<char> > vlin(line, sep);
    auto it = vlin.begin();

    //load the values in the line
    for(int i=0; i<lsiz; i++) {
      istringstream st(*it++);
      st >> val[i];
    }

    //HepMC3 event
    GenEvent evt(Units::GEV, Units::MM);
    evt.set_event_number(iev-1);

    //photon location, mm
    evt.shift_position_to( FourVector(val[iposx]*10, val[iposy]*10, invert_z*val[iposz]*10, 0) );

    //photon particle, GeV
    FourVector vec(val[idirx]*val[ien]*1e-9, val[idiry]*val[ien]*1e-9, invert_z*val[idirz]*val[ien]*1e-9, val[ien]*1e-9);
    GenParticlePtr p0 = std::make_shared<GenParticle>(vec, 22, 1);
    evt.add_particle(p0);

    //flux
    std::shared_ptr<Attribute> aflux = std::make_shared<DoubleAttribute>( val[iflux] );
    evt.add_attribute("Flux_[photon/s]", aflux);

    //power
    std::shared_ptr<Attribute> apower = std::make_shared<DoubleAttribute>( val[ipower] );
    evt.add_attribute("Power_[W]", apower);

    file.write_event(evt);

  }//input loop

  file.close();
  in.close();

  return 0;

}//main

//_____________________________________________________________________________
map<string, int> get_header(ifstream &in) {

  //input header from the first line
  string line;
  getline(in, line);

  //split the line
  char_separator<char> sep(",");
  tokenizer< char_separator<char> > cline(line, sep);

  //fill the header
  map<string, int> header;
  int i=0;
  for(auto it = cline.begin(); it != cline.end(); it++) {
    if( (*it).size() == 1 ) continue; // skip the last empty item

    header[*it] = i++;
  }

  return header;

}//get_header
































