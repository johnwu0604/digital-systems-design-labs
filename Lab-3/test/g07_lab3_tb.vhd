library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package coefficient_input_type is
   type c_input is array (0 to 24) of unsigned(15  downto 0);
end package coefficient_input_type;

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.coefficient_input_type.all;
use std.textio.all;
use ieee.std_logic_textio.all;

entity g07_lab3_tb is 
end g07_lab3_tb;

architecture test of g07_lab3_tb is 

component g07_FIR is 
	port(x		:in std_logic_vector(15 downto 0);
	     y		:out std_logic_vector(16 downto 0);
	     c          :in c_input;
	     clk	:in std_logic;
	     rst	:in std_logic);
end component g07_FIR;


file file_VECTORS_X : text;
file file_RESULTS   : text;
file file_COEFF   : text;

constant clk_PERIOD	:  time  := 120 ns;

signal x_in	: std_logic_vector(15 downto 0);
signal y_out 	: std_logic_vector(16 downto 0);
signal c_in : c_input;
signal clk_in 	: std_logic;
signal rst_in	: std_logic;



begin 

g07_FIR_INST : g07_FIR
	port map (
		x => x_in,
		y => y_out,
		c => c_in,
		clk => clk_in,
		rst => rst_in
		);
clk_generation : process
begin
	clk_in <='1';
	wait for clk_PERIOD / 2;
	clk_in <='0';
	wait for clk_PERIOD / 2;
end process clk_generation;


feeding_inst: process is

	variable v_Iline1 : line;
	variable v_Cline1 : line;
	variable v_Oline : line;
	variable v_x_in 	: std_logic_vector(15 downto 0);
        variable v_c_in: std_logic_vector(15 downto 0);
   begin
	rst_in <='1';
	wait until rising_edge(clk_in);
	wait until rising_edge(clk_in);
	rst_in  <='0';


	file_open(file_VECTORS_X, "lab3-in.txt", read_mode);
	file_open(file_RESULTS, "lab3-out.txt", write_mode);
	file_open(file_COEFF, "lab3-coeff.txt", read_mode);
	
	for I in 0 to 24 loop
	    if not endfile(file_COEFF) then		
 		readline(file_COEFF, v_Cline1);
		read(v_Cline1, v_c_in);
 		c_in(I) <= unsigned(v_c_in);
	    end if;
	end loop;

	while not endfile(file_VECTORS_X) loop
	
		readline(file_VECTORS_X, v_Iline1);
		read(v_Iline1, v_x_in);

		x_in <= v_x_in;
		
		
		 write(v_Oline, y_out);
	   	writeline(file_RESULTS, v_Oline);
		wait until rising_edge(clk_in);
	end loop;
	wait until rising_edge(clk_in);
	wait until rising_edge(clk_in);
	wait;
	 
end process feeding_inst;

end test;