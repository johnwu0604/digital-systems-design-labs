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

entity g07_lab4 is
	port ( x : in std_logic_vector(15 downto 0);
	       c : in c_input;
			 clk, rst: in std_logic; 
			 y : out std_logic_vector(16 downto 0));
end g07_lab4;

architecture details of g07_lab4 is

   type input_array is array(0 to 24) of unsigned(16 downto 0);
   type input_array_long is array(0 to 24) of unsigned(31 downto 0);

   signal input: input_array;
   signal input_long: input_array_long;

begin
	
	fir_process : process (rst,clk)
                variable current_input: unsigned(15 downto 0);
		begin
		  if(rst='1') then
			 input <=  (others=>(others=>'0'));
		  elsif(rising_edge(clk)) then
			 current_input := unsigned(x);
			 input_long(0) <= current_input * c(0);
			 input(0) <= unsigned(input_long(0)(31 downto 15));
			 for I in 1 to 24 loop
				input_long(I) <= input_long(I-1) + current_input*c(I);
				input(I) <= unsigned(input_long(I)(31 downto 15));          
			 end loop;			
		  end if; 
		  y <= std_logic_vector(input(24));	
		end process fir_process;

end details;