library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
entity g07_lab1 is
	Port (	clk, direction, rst, enable: in std_logic;
				output: out std_logic_vector(7 downto 0));
end g07_lab1;

architecture bitCounter of g07_lab1 is

signal count: integer range 0 to 255;

begin
output <= std_logic_vector(to_unsigned(count,8)) ;
counter1: process(clk)
	begin 
		if rising_edge(clk) then
			if rst = '1' then
				count <= 0;
			elsif enable = '1' then
				if direction = '1' then count <= count + 1;
				else count <= count - 1;
				end if; 
			end if;
		end if;
	end process;
end bitCounter;
				
