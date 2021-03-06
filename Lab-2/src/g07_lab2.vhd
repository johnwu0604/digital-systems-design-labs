library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity g07_lab2 is
	port(x: in std_logic_vector(9 downto 0);
		  y: in std_logic_vector(9 downto 0);
		  N: in std_logic_vector(9 downto 0);
		clk: in std_logic;
		rst: in std_logic;
		mac: out std_logic_vector(20 downto 0);
		ready: out std_logic);
end g07_lab2;
		
architecture details of g07_lab2 is
signal temp:  std_logic_vector(20 downto 0);
begin
	process(clk,rst)
	begin
      ready <= '1';
		if (rst = '1') then
			temp <= (others => '0');
		elsif(rising_edge(clk)) then
		   temp <= std_logic_vector(unsigned(temp) + unsigned(unsigned(x)*unsigned(y)));
		end if;
   end process;
   mac <= temp;
end details;