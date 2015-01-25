function testClassPredicted=getLabel(Y)
% obtain class labels from Y, called by logistic regression
% for example
% Y, n by k matrix, it can be posterior probability
% testClassPredicted: n by 1 vector, intiger, each element is from {1,2,...,k}
%%%%
% Copyright (C) <2012>  <Yifeng Li>
% 
% This program is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% any later version.
% 
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
% 
% You should have received a copy of the GNU General Public License
% along with this program.  If not, see <http://www.gnu.org/licenses/>.
% 
% Contact Information:
% Yifeng Li
% University of Windsor
% li11112c@uwindsor.ca; yifeng.li.cn@gmail.com
% July 04, 2012
%%%%

numObs=size(Y,1);
testClassPredicted=nan(numObs,1);
for i=1:numObs
     [valp,indp]=max(Y(i,:));
     testClassPredicted(i)=indp;
end