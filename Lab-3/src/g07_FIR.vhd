library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package coefficient_input_type is
   type c_input is array (0 to 24) of signed(15  downto 0);
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

   type coefficient_input is array (0 to 24) of signed(15  downto 0);
   type data_pipe_input is array (0 to 24) of signed(15  downto 0);
   type multiply_input is array (0 to 24) of signed(31    downto 0);
   type add_input is array (0 to 1) of signed(32  downto 0);

	signal coefficient : coefficient_input;
   signal data_pipe : data_pipe_input;
   signal multiply : multiply_input;
   signal add0 : add_input;
   signal add1 : signed(33  downto 0);

begin
	
	p_input : process (rst,clk)
		begin
		  if(rst='1') then
			 data_pipe <= (others=>(others=>'0'));
			 coefficient <= (others=>(others=>'0'));
		  elsif(rising_edge(clk)) then
			 data_pipe <= signed(x)&data_pipe(0 to data_pipe'length-2);
			 for I in 0 to 24 loop
				coefficient(I) <= signed(c(I));
			 end loop;			 
		  end if;
		end process p_input;
		
	p_mult : process (rst,clk)
		begin
		  if(rst='1') then
			 multiply <= (others=>(others=>'0'));
		  elsif(rising_edge(clk)) then
			 for k in 0 to 24 loop
				multiply(k) <= data_pipe(k) * coefficient(k);
			 end loop;
		  end if;
		end process p_mult;
		
	p_add0 : process (rst,clk)
		begin
		  if(rst='1') then
			 add0 <= (others=>(others=>'0'));
		  elsif(rising_edge(clk)) then
			 for k in 0 to 1 loop
				add0(k) <= resize(multiply(2*k),33)+resize(multiply(2*k+1),33);
			 end loop;
		  end if;
		end process p_add0;
		
	p_add1 : process (rst,clk)
		begin
		  if(rst='1') then
			 add1 <= (others=>'0');
		  elsif(rising_edge(clk)) then
			 add1 <= resize(add0(0),34) + resize(add0(1),34);
		  end if;
		end process p_add1;
		
	p_output : process (rst,clk)
		begin
		  if(rst='1') then
			 y <= (others=>'0');
		  elsif(rising_edge(clk)) then
			 y <= std_logic_vector(add1(33 downto 17));
		  end if;
		end process p_output;
		
end details;