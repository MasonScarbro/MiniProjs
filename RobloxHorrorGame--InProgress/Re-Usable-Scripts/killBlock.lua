local killBlock = script.Parent

killBlock.Touched:Connect(function(whatTouched) -- the connect feature here figures out what touched it, just like last Time it is not a normal function teh parameter only exists because of the API because touched:connect returns what touched 
	if whatTouched.Parent:FindFirstChild("Humanoid") then -- if what touched its parent is a humanoid (all players have a humanoid part) and its children are its body parts like feet 
		whatTouched.Parent.Humanoid.Health = 0 -- kill him
	end
end)

-- OMMIT BELOW FOR SIMPLE KILLBLOCK

local vctrZ = 2 -- this is just the vector size I want to be the base
while true do
	wait(.5) -- the time between executions so the block only expands every .5 seconds
	killBlock.Size = Vector3.new(23, 1, vctrZ) -- sets the new scale value each time 
	vctrZ += 1 -- incrementer
	if vctrZ == 24 then -- if it reaches the max reset
		vctrZ = 2 -- org value
	end
end

-- Side Notes: Alternativley by incrementing the specific size itself we can create a inflating and deflating box
-- Like this killBlock.Size.Z -= 1 when it reaches desired value and otherwise +=
