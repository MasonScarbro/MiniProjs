local floor = game.Workspace.DanceFloor -- lets the variable floor equal the DanceFlorr folder

while true  do
	task.wait(1) -- waits one sec before changing colors 
	for _, part in floor:GetChildren()  do -- for each part (can be v or anything) in the DanceFloor folder i.e get children preform this task
		local r = math.random(40, 244)
		local g = math.random(32, 254)
		local b = math.random(88, 232)
		
		part.Color = Color3.fromRGB(r, g, b)
	end
end
