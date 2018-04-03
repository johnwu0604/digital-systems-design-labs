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

entity g07_FIR is
	port ( x : in std_logic_vector(15 downto 0);
	       c : in c_input;
			 clk, rst: in std_logic; 
			 y : out std_logic_vector(16 downto 0));
end g07_FIR;

architecture details of g07_FIR is

   signal input: std_logic_vector(15 downto 0);
   signal output : std_logic_vector(31 downto 0);

begin
	
	fir_process : process (rst,clk)
		begin
		  if(rst='1') then
			 output <= (others=>'0');
		  elsif(rising_edge(clk)) then
			 input <= x;
			 output <= std_logic_vector(unsigned(input) * c(0));
			 for I in 1 to 24 loop
				output <= std_logic_vector(unsigned(output) + unsigned(input) * c(I));
			 end loop;			 
		  end if;
		  y <= output(31 downto 15);
		end process fir_process;

end details;
