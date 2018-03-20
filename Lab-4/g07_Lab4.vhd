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

entity g07_Lab4 is
	port ( x : in std_logic_vector(15 downto 0);
	       --c : in c_input;
			 clk, rst: in std_logic; 
			 y : out std_logic_vector(16 downto 0));
end g07_Lab4;

architecture details of g07_Lab4 is

   type input_array is array(0 to 24) of unsigned(15 downto 0);

	signal c: c_input;
   signal input: input_array;
   signal output : unsigned(31 downto 0);

begin
	
	fir_process : process (rst,clk)
		begin
		  if(rst='1') then
			 output <= (others=>'0');
			 input <=  (others=>(others=>'0'));
		  elsif(rising_edge(clk)) then
			 input(0) <= unsigned(x);
			 output <= input(0) * c(0);
			 for I in 1 to 24 loop
				output <= output + input(I) * c(I);
            input(I) <= input(I-1);
			 end loop;			
		  end if;
		  y <= std_logic_vector(output(31 downto 15));
		end process fir_process;

end details;