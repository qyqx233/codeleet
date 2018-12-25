-- local lfs_ffi = require "lfs_ffi"
-- local ffi = require "ffi"
-- for i in lfs_ffi.dir('.')
-- do
    -- print(i)
-- end
local c1 = os.clock()
for i=1, 100000
do
    os.sleep(1)
end
local c2 = os.clock()
print(c2 - c1)
-- local s = [[
--     hello
--     world
-- a]]
-- print(s)

-- function add(a, ...)  
--     local s = 0  
--       for i, v in ipairs{...} do   --> {...} 表示一个由所有变长参数构成的数组  
--         s = s + v  
--       end  
--       return s  
-- end  
-- local byte, char = string.byte, string.char
-- local function foo(x)
--   return char(byte(x)+1)
-- end
-- print(char(49))
local s = "阿斯大法"
for i = 1,#s do
    -- print(string.byte(s, i))
end