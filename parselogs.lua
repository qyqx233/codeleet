local lfs = require "lfs"
function getpathes(rootpath, handle)
    pathes = pathes or {}
    for entry in lfs.dir(rootpath) do
        if entry ~= '.' and entry ~= '..' then
            local path = rootpath .. '//' .. entry
            local attr = lfs.attributes(path)
            assert(type(attr) == 'table')

            if attr.mode == 'directory' then
                getpathes(path, handle)
            else
                -- handle(rootpath, entry)
                table.insert(pathes, {rootpath, entry, attr})
            end
        end
    end
    return pathes
end

local path = arg[1]

pathes = getpathes(path, nil)

for i,j in ipairs(pathes) do
end