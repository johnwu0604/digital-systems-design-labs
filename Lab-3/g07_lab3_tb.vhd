
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use STD.textio.all;
use ieee.std_logic_textio.all;

entity g07_lab3_tb is 
end g07_lab3_tb;

architecture test of g07_lab3_tb is 

component g07_FIR is 
	port(x		:in std_logic_vector(15 downto 0);
	     y		:out std_logic_vector(32 downto 0);
	     clk	:in std_logic;
	     rst	:in std_logic);
end component g07_FIR;

constant clk_PERIOD	:  time  := 120 ns;

signal x_in	: std_logic_vector(15 downto 0);
signal y_out 	: std_logic_vector(32 downto 0);
signal clk_in 	: std_logic;
signal rst_in	: std_logic;

begin 

g07_FIR_INST : g07_Lab3
	port map (
		x => x_in,
		y => y_out,
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

file file_VECTORS_X : text;
file file_RESULTS   : text;

feeding_inst: process is

	variable v_Iline1 : line;
	variable v_Oline : line;
	variable v_x_in 	: std_logic_vector(15 downto 0);
   begin
	rst_in <='1';
	wait until rising_edge(clk_in);
	wait until rising_edge(clk_in);
	rst_in  <='0';


	file_open(file_VECTORS_X, "lab3-in.txt", read_mode);
	file_open(file_RESULTS, "lab3-out.txt", write_mode);

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
	 
end process feeding_inst;

end test;