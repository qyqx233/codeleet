function findTwo(s, b, e, fn)
    local offset = 1
    local p = b
    local lastBeginPos
    while true do
        local beginPos, endPos = string.find(s, p, offset)
        if beginPos == nil then
            if p == e then
                fn(s, beginPos, string.len(s))
                break
            else
                break
            end
        end
        if p == e then
            fn(string.sub(s, lastBeginPos, endPos))
        end
        lastBeginPos = beginPos
        offset = endPos + 1
        if p == b then p = e else p = b end
    end

end

local file = io.open("1.log", "r")
local s = file:read("*a")
function foo(s)
    print(s)
end
findTwo(s, "log start", "log end", foo)
file:close()